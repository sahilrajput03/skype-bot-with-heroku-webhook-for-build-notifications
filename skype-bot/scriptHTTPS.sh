#!/usr/bin/env bash
# set -a make all the variables defined to accessible by sub shell scripts/programs ~Sahil
set -a
. .env
source venv/bin/activate
# source: https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
# flask run --cert=adhoc --host=0.0.0.0
# below would use real ssl certs generated by `certbot` cli by letsencrypt:
flask run --cert=./my-site-certs/fullchain.pem --key=./my-site-certs/privkey.pem --host=0.0.0.0

