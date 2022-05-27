#!/bin/bash

echo 'Initialize Python virtual environment'
python -m venv .venv

echo 'Activate Python virtual environment'
source .venv/bin/activate

echo 'Installing dependencies'
git clone https://github.com/lalitshankarchowdhury/bme68x-python-library
.venv/bin/python3 bme68x-python-library/setup.py
pip install -r requirements.txt