#!/bin/bash

python3 -m pip install --upgrade build
pip install virtualenv
pip install --upgrade pip
pip install --upgrade wheel
pip install --upgrade setuptools

if [ -d "dist" ]
then
    rm -rf dist
    mkdir dist
else
    mkdir dist
fi

python3 -m build
# python3 setup.cfg install
# python3 setup.cfg bdist_wheel -w dist
