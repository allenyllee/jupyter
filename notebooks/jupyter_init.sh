#!/bin/bash

if [ -e ~/.jupyter/jupyter_notebook_config.py ]
then
    echo "already init..."
else
    echo "init password..."
    jupyter notebook --allow-root --generate-config
    python3 ./JupyterPassword.py
fi
