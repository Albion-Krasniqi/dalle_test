#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo [$(date)]: "START"

# Check if conda is installed
if ! command -v conda &> /dev/null
then
    echo "Conda could not be found. Please install Conda and try again."
    exit
fi

echo [$(date)]: "Creating conda env with python 3.9"
conda create --prefix ./env python=3.9 -y

echo [$(date)]: "Activating the environment"
# Use the correct activation command for conda on macOS
source activate ./env || conda activate ./env

echo [$(date)]: "Installing the requirements"
pip install -r requirements.txt

echo [$(date)]: "END"