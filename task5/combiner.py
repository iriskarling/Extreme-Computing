#!/usr/bin/env python2
# combiner.py
import sys
earliest_year = 2129
latest_year = 0

for line in sys.stdin:
    # Parse key and value
    a = int(line)
    if a < earliest_year:
        earliest_year = a #get the earliest_year
    if a > latest_year:
        latest_year = a #get the latest_year
print (str(earliest_year)+'\t'+str(latest_year))
