#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <search parameter>"
    exit 1
fi

python main.py "$@"
