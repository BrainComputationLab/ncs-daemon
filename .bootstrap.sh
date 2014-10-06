#!/bin/bash

# create and enter virtualenv
if [ ! -d ".env" ]; then
  virtualenv .env
fi
. .env/bin/activate

# required dirs
if [ ! -d "logs" ]; then
  mkdir logs
fi

# install requirements
pip install -r requirements-test.txt
pip install -r requirements-docs.txt
pip install -r requirements.txt
python setup.py install

# update ncs
git submodule update --init
touch ncs/base/__init__.py ncs/base/pyncs.py
sudo mkdir -p /var/ncs
sudo chown -f ${USER}:${USER} /var/ncs
