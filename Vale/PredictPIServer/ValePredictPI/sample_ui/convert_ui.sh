#!/bin/bash

INPUT_NAME=$(tr '.' '_' <<< "${1}")
pyuic5 ${1} > $INPUT_NAME.py
