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
pip install -r requirements-dev.txt
pip install -r requirements.txt
python setup.py install

# install nvm
#git clone https://github.com/creationix/nvm.git ~/.nvm
#source ~/.nvm/nvm.sh
#sudo mkdir /var/ncs
#nvm install 0.10
#nvm use 0.10
#npm install -g jsontools

# update ncs
git submodule update --init
touch ncs/base/__init__.py ncs/base/pyncs.py
sudo mkdir -p /var/ncs
sudo chown -f ${USER}:${USER} /var/ncs
