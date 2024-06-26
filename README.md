# python-mdd


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Install

``` sh
pip install python_mdd
```

## How to use

The API documentation is auto-generated by nbdev/Quarto and hosted on
[GitHub Pages](https://rkimura47.github.io/python-mdd/).

Fill me in please! Don’t forget code examples:

``` python
1+1
```

    2

## Development

This repo is set up using [nbdev](https://nbdev.fast.ai/), a Jupyter
notebook-driven software development platform especially suited to
creating Python packages with extensive, high-quality documentation.
Additionally, the [Docker](https://docs.docker.com/manuals/) files
provide a complete containerized JupyterLab environment for development.

At a high level, the development workflow of nbdev can be summarized as
follows:

1.  Directly edit module source code / documentation in notebook files
    in `nbs/`.
2.  “Restart the kernel and run all cells” to run the entire Notebook
    and check for errors.
3.  Check the generated documentation via `nbdev_preview`.
4.  Once you’re ready to commit changes, run the entire notebook, save,
    close it, then confirm via Git.
    1.  You can also manually run `nbdev_prepare` and
        `pre-commit run --all-files`.

Notably, `README.md` and the files in `python_mdd/` should NOT be
manually edited; instead, they should be generated based on notebook
files in `nbs/`.

See the [nbdev documentation](https://nbdev.fast.ai/tutorials/) for
additional details on software development using nbdev.

To spin up the containerized JupyterLab server, run (from the repo root)

``` sh
docker compose up server
```

To take it down, run (from the repo root)

``` sh
docker compose down
```

Some notable quirks of this particular containerized setup:

- [pre-commit](https://pre-commit.com/) is configured to enforce
  type-checking and linting. In particular, **`.git/hooks/pre-commit` is
  OVERWRITTEN on container start-up**. If you wish to customize
  `pre-commit` (or disable it), you can do so by modifying
  `docker/start-notebook.d/20-configure-pre-commit.sh` or adding
  additional startup scripts.
- `nbdev_preview` is configured to output to `0.0.0.0:3000` (and will
  say so in the console output), but it’s actually outputting to
  `localhost:3000` (from the perspective of the host machine). This is
  due to the command being run from within a container.
- The outputs of Jupyter notebooks are cleaned on save via nbdev’s
  Jupyter hook. Note that this may not be (is usually not) immediately
  reflected in the JupyterLab web interface.
- On container start-up, the repo package is installed in editable mode
  with the command `pip install -e '.[dev]'` to ensure it can be
  accessed from any notebook.

Alternatively, any software development environment set up to work with
the nbdev platform should also be sufficient.

### Notes on accessing host SSH credentials from within a container

You may want to access your host SSH credentials from within the
container if you are using pre-commit with the containerized
environment. Unfortunately this can be tricky to set up (especially on
Windows), and the details are far beyond the scope of this README.

That said, one relatively straightforward method is to specify a private
`compose.override.yaml` file to mount the necessary SSH files. The
following links may provide some guidance on specifics:

- https://blog.gabrielmajeri.ro/2022/01/21/how-to-share-ssh-credentials-between-windows-and-wsl-2.html
- https://skyraptor.eu/blog/seamless-integration-using-windows-ssh-keys-and-ssh-agent-in-wsl2
- https://docs.docker.com/desktop/networking/#ssh-agent-forwarding
- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials
