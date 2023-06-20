#!/usr/bin/env bash

# Install Python and the pip package manager.
apt-get install -y python3 python3-pip python3-dev

# Install required packages.
pip3 install -r /autograder/source/requirements.txt