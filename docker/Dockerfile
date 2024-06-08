# Based on Dockerfile for scipy-notebook
# https://github.com/jupyter/docker-stacks/blob/main/images/scipy-notebook/Dockerfile

# For image contents, see https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-minimal-notebook
FROM quay.io/jupyter/minimal-notebook:x86_64-2024-02-13

USER root

# Quarto cannot be installed via mamba or pip.
RUN curl -Lo /tmp/quarto.deb https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.554/quarto-1.4.554-linux-amd64.deb
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends /tmp/quarto.deb && \
    rm /tmp/quarto.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# Install Python 3 packages
RUN mamba install --yes \
    'fastai::nbdev' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Some packages cannot be installed with mamba.
RUN pip install --no-cache-dir \
    'jupyterlab-quarto' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install Git-friendly Jupyter hooks
RUN nbdev_install_hooks && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install startup scripts
COPY --chown=${NB_UID}:${NB_GID} docker/install-package-editable.sh /usr/local/bin/start-notebook.d/

USER ${NB_UID}

WORKDIR "${HOME}"
