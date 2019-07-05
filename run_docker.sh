#!/usr/bin/env bash
set -e
mkdir -p "volumes/elasticsearch/data"
CURRENT_UID="$(id -u):$(id -g)" docker-compose up $*
