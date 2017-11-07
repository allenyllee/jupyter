#!/bin/bash

# 
# add module search path NODE_PATH
# npm - node.js modules path - Stack Overflow 
# https://stackoverflow.com/questions/13465829/node-js-modules-path
# 
NODE_PATH=$(npm root -g)
export NODE_PATH

node $@
