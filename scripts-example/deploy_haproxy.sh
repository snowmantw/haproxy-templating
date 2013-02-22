#!/bin/sh

# Setup paths and run it.

TPLDIR=~/haproxy-templating
HACMD=/usr/local/bin/haproxy_wrapper.sh
CONFIG=~/ejabberd.cfg
NODELIST=~/nodes.csv
PYTHON=python

$PYTHON $TPLDIR/main.py $HACMD $CONFIG $NODELIST
