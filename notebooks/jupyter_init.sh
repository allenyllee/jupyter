#!/bin/bash

# source directory of this script
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -e ~/.jupyter/jupyter_notebook_config.py ]
then
    echo "already install jupyter..."
    echo "already init password..."
    echo "starting jupyter..."
    /opt/conda/bin/jupyter notebook --allow-root --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser
else
    echo "install jupyter..."
    /opt/conda/bin/conda install jupyter -y --quiet
    echo "init password..."
    jupyter notebook --allow-root --generate-config
    python3 $SOURCE_DIR/JupyterPassword.py
    echo "starting jupyter..."
    /opt/conda/bin/jupyter notebook --allow-root --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser
fi
