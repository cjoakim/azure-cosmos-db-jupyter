#!/bin/bash

# List the defined jupyter kernels on your system and add current directory.
# Chris Joakim

# activate the python venv
source venv/bin/activate
python --version

jupyter kernelspec list

# Install the current directory as a kernel 
jupyter kernelspec install-self

jupyter kernelspec list
