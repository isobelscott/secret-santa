#!/usr/bin/env bash

# run in a container
docker-compose \
    --env-file $DIR/secrets.props \
    -force-recreate \
    up