#!/bin/bash
# Install this repo's Python package to the current environment, for development purposes.
cd "${HOME}/python-mdd"; pip install -e '.[dev]'
