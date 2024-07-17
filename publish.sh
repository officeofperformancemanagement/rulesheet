#!/bin/sh -e

#echo "test once again"
python3 test.py

python3 -m pip install --upgrade twine

python3 -m twine check dist/*

python3 -m twine upload dist/*