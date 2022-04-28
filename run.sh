#!/bin/bash

# set .env vars
export $(echo $(cat ./config/.env | sed 's/#.*//g'| xargs) | envsubst)

docker-compose -f docker-compose.yml -p recipes-information-system up -d --build
