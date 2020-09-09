#!/bin/sh
# Exports env variables.
# chmod +x export.sh
# Usage: ./export.sh /path/to/.env

export $(cat $1 | sed 's/#.*//g' | xargs)
