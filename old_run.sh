#!/bin/bash

export FLASK_APP=src/server/main
export DEBUG=true

flask run --host localhost --port 8080
