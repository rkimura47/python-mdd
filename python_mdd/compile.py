# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_compile.ipynb.

# %% auto 0
__all__ = ['compile_top_down']

# %% ../nbs/01_compile.ipynb 3
from collections.abc import Callable, Collection, Sequence
from .mdd import DEFAULT_MDD_NAME, MDD, MDDArc, MDDArcData, MDDNode, MDDNodeState
from random import sample
from typing import Optional

# %% ../nbs/01_compile.ipynb 6
def compile_top_down(
    num_layers: int, # number of (arc) layers, i.e., variables
    domain_function: Callable[[int], list[int]], # function specifying the domain of each layer
    transition_function: Callable[[MDDNodeState, int, int], MDDNodeState], # function specifying the state transitions
    arc_data_function: Callable[[MDDNodeState, int, int, MDDNodeState], MDDArcData], # function specifying arc data
    root_state: MDDNodeState, # state of the root node
    is_feasible: Callable[[MDDNodeState, int], bool], # function that determines whether a node state is feasible
    max_width: Optional[Callable[[int], float]] = None, # function specifying the maximum width of each layer
    merge_function: Optional[Callable[[Collection[MDDNodeState], int], MDDNodeState]] = None, # function that determines how to merge node states
    arcdata_function: Optional[Callable[[MDDArcData, MDDNodeState, MDDNodeState, int], MDDArcData]] = None, # function specifying the arc data
    node_selection_function: Optional[Callable[[Sequence[MDDNode], int], list[MDDNode]]] = None, # function specifying nodes to select for merge / removal
    name: str = DEFAULT_MDD_NAME, # name of MDD
) -> MDD: # Compiled decision diagram
    # Basic parameter checks  and default settings
    if max_width is None:
        max_width = lambda j: float("inf")
        node_selection_function = lambda slist,j: list(slist)
    else:
        if merge_function is None != arcdata_function is None:
            raise RuntimeError("merge_function and arcdata_function must be defined together")
        if node_selection_function is None:
            node_selection_function = lambda slist,j: sample(slist, 1 + int(merge_function is not None))

    # Create first layer, containing only the root
    mdd = MDD()
    mdd.append_new_layers(num_layers+1)
    mdd.add_node(MDDNode(0, root_state))

    # Create rest of the layers in a top-down fashion
    for j in range(num_layers):
        # Merge / Remove until current layer is under max_width
        curr_layer = [u for u in mdd.allnodes_in_layer(j)]
        curr_width = len(curr_layer)
        max_allowed_width = max_width(j)
        while curr_width > max_allowed_width:
            mnodes = node_selection_function(curr_layer, j)
            if merge_function is None:  # Remove
                mdd.remove_nodes(mnodes)
            else:                       # Merge
                mdd.merge_nodes(mnodes, j, merge_function, arcdata_function)
            curr_layer = [u for u in mdd.allnodes_in_layer(j)]
            if len(curr_layer) >= curr_width:
                raise RuntimeError("No more nodes to remove/merge but width of layer %d > %d" % (j, max_allowed_width))
            curr_width = len(curr_layer)

        # For each node in the current layer and each possible assignment
        for u in mdd.allnodes_in_layer(j):
            for d in domain_function(j):
                # Apply transition function
                vstate = transition_function(u.state, d, j)
                # Add if node is feasible
                if is_feasible(vstate, j+1):
                    v = MDDNode(j+1, vstate)
                    # Check if equivalent node exists
                    if v not in mdd.allnodes_in_layer(j+1):
                        mdd.add_node(v)
                    # Add appropriate arc
                    mdd.add_arc(MDDArc(d, u, v), arc_data_function(u.state, d, j, vstate))
    return mdd