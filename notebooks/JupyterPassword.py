#!/usr/bin/env python3

"""
Script to create a password for the Jupyter notebook configuration
Written by Pieter de Rijk <pieter@de-rijk.com>
"""

import os
from notebook.auth import passwd


JUPYTER_CONFIG = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')
LINE = "==========================================================================="

print(LINE)
print("Setting Jupyter additional configuration")
print(LINE)

if 'PASSWORD' in os.environ:
    PSWD = os.environ['PASSWORD']
    if PSWD:
        print("PASSWORD environment varible has been set, just use it....")
        PWHASH = passwd(PSWD)
    else:
        print("Please set a strong password")
        PWHASH = passwd()
    del os.environ['PASSWORD']

print(LINE)
print("Following will be added to %s " % (JUPYTER_CONFIG))

JUPYTER_COMMENT_START = "# Start of lines added by jupyter-password.py"
JUPYTER_COMMENT_END = "# End lines added by jupyter-passwordd.py"
JUPYTER_PASSWD_LINE = "c.NotebookApp.password = u'%s'" % (PWHASH)
JUPYTER_NO_BROWSER = "c.NotebookApp.open_browser = False"

print(" ")
print("  %s " % (JUPYTER_COMMENT_START))
print("  %s " % (JUPYTER_PASSWD_LINE))
print("  %s " % (JUPYTER_NO_BROWSER))
print("  %s " % (JUPYTER_COMMENT_END))
print(LINE)

with open(JUPYTER_CONFIG, 'a') as file:
    file.write('\n')
    file.write(JUPYTER_COMMENT_START + '\n')
    file.write(JUPYTER_PASSWD_LINE + '\n')
    file.write(JUPYTER_NO_BROWSER + '\n')
    file.write(JUPYTER_COMMENT_END + '\n')
