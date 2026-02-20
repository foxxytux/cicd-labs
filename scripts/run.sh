#!/bin/bash

for py_file in $(find ../production -name "*.py")
do
    python3 $py_file
done
