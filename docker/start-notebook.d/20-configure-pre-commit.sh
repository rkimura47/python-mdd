#!/bin/bash
# Install pre-commit hooks to enforce type-checking and linting.
cd "${HOME}/python-mdd"; pre-commit install --overwrite
