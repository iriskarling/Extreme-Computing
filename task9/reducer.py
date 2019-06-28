#!/usr/bin/env python2
# reducer.py
import sys

prev_key = None
count = 1

for line in sys.stdin:
    # Parse key and value
    g= line.strip()
    if g == prev_key and prev_key is not None:
        count += 1
    elif g != prev_key and prev_key is not None:
        print(str(prev_key)+'\t'+str(count)) #genres/ count of genres
        count =1
    prev_key = g

if prev_key is not None:
    print(str(prev_key)+'\t'+str(count))
