#!/usr/bin/env bash
# set -a make all the variables defined to accessible by sub shell scripts/programs ~Sahil
set -a
. .env
source venv/bin/activate
flask run --host=0.0.0.0
