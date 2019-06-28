#!/usr/bin/env python2
# reducerb.py
import sys

prev_key = None
prev_rate = 0
count =0
num = 1
for line in sys.stdin:
    t,rating = line.strip().split('\t')
    if t == prev_key and prev_key is not None:
        count += float(prev_rate)
        num += 1
    elif t != prev_key and prev_key is not None:
        if num ==1:
            count =float(prev_rate)
            avg = count/num
            avg = round(avg,1)
        else:
            count += float(prev_rate)
            avg = count/(num)
            avg = round(avg,1)
        print(str(prev_key)+'\t'+str(avg)) # decade /average
        num = 1
        count = 0

    prev_key = t
    prev_rate = rating
