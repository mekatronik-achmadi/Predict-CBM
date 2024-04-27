#!/bin/bash

sshfs  -o rw,uid=$UID \
    pclab@10.160.10.211:/home/development/Packages/Vale/OlahData \
    ./datamount/

