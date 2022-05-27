#!/bin/bash

echo 'Deactivate Python virtual environment (if already present)'
if [[ "$VIRTUAL_ENV" != "" ]]
then
  deactivate
fi

echo 'Initialize new Python virtual environment'
python -m venv .venv

echo 'Activate Python virtual environment'
source .venv/bin/activate

echo 'Install dependencies'
git clone https://github.com/lalitshankarchowdhury/bme68x-python-library
cd bme68x-python-library/
../.venv/bin/python3 setup.py install
cd ..
pip install -r requirements.txt