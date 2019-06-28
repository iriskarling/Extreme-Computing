#!/usr/bin/env python2
# combiner.py
import sys

for line in sys.stdin:
    # Parse key and value
    g, year= line.strip().split('\t')
    if int(year) >= 2000 and int(year) <= 2014:
        print(str(g)) #genres
