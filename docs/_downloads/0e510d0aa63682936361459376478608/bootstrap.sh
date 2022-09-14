#!/bin/bash

# SYSTEM DEPENDENCIES

# APP DEPENDENCIES
python3 -m venv .env
source .env/bin/activate
python setup.py install
