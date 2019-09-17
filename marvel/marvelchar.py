#!/usr/bin/env python3
import argparse
import time
import hashlib

import requests

## Define the API here
CHAR = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(tim, pvkee, pubkee):
    return hashlib.md5((tim + pvkee + pubkee).encode('utf-8')).hexdigest()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookup):
    r = requests.get(CHAR+"?name="+lookup+"&ts="stampystamp+"&apikey="pkeyz+"&hash="+hashyhash)
