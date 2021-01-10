#!/usr/bin/env bash

# run in a container
docker-compose \
    --env-file $DIR/dev.env \
    -force-recreate \
    up