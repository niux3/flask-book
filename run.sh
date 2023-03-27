#!/bin/bash

if [ ! -d ".venv" ]
then
    mkdir .venv && pipenv run python -m venv ./.venv && . .venv/bin/activate && pipenv install 
fi
. .venv/bin/activate && flask run -p 8000
