#!/bin/sh
export FLASK_APP=./src/main/python/server/main.py
export FLASK_ENV=production
flask run