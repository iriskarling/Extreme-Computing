#!/usr/bin/env python2
# reducer.py
import sys
earliest_year = 2129
latest_year = 0

for line in sys.stdin:
    # Parse key and value
    el, ly= line.strip().split('\t')
    a = int(el)
    b = int(ly)
    if a < earliest_year:
        earliest_year = a #get the earliest_year
    if b > latest_year:
        latest_year = b #get the latest_year
print (str(earliest_year)+'\t'+str(latest_year)), #print the result
