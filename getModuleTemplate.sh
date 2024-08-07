#!/bin/bash

# Check if an argument was passed
if [ $# -eq 0 ]; then
    echo "No arguments provided."
    exit 1
fi

# The first argument
ARGUMENT=$1

RESULT=$(python3 /home/wombat/repos/verilogThings/getModuleTemplate.py "$ARGUMENT")

# Print the argument
echo "Argument passed: $RESULT"
