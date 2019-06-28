#!/usr/bin/env python2
# combiner.py
import sys

prev_key = None
num = 1
for line in sys.stdin:
    stro,count= line.strip().split('\t')
    if stro == prev_key and prev_key is not None:
        num += int(count)             #count the number of string
    elif stro != prev_key and prev_key is not None:
        print(str(prev_key)+'\t'+str(num))
        num = int(count)
    prev_key = stro

if prev_key is not None:
    print(str(prev_key)+'\t'+str(num))
