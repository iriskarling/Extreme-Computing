#!/usr/bin/env python2
# reducer.py
import sys

prev_key = None
prev_value = None
for line in sys.stdin:
    id_num,attribute,t = line.strip().split('\t')
    #print("id:",id_num)
    #print("prev_key",prev_key)
    if id_num == prev_key and prev_key is not None and prev_value is not None:
        if t == "year":
            print(str(attribute)+'\t'+str(prev_value)) # year /averageRating
        else:
            print(str(prev_value)+'\t'+str(attribute)) # year /averageRating
    prev_key = id_num
    prev_value = attribute
