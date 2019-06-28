#!/usr/bin/env python2
# reducer.py
import sys


prev_key = None

for line in sys.stdin:
    # Parse key and value
    key= line
     # If key has changed then one can finish processing the previoos key
    if key != prev_key and prev_key is not None:
        print(prev_key),
    prev_key = key

if prev_key is not None:
    print(prev_key),
