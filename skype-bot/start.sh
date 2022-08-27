#!/usr/bin/env bash
# set -a make all the variables defined to accessible by sub shell scripts/programs ~Sahil
set -a
. .env
source env/bin/activate
python3 a.py
