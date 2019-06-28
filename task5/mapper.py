#!/usr/bin/env python2
# mapper.py
import sys

i = 0

for line in sys.stdin:
    # Call map_function for each line in the input
    if i >= 1:
        ls =[]
        for word in line.split('\t'):
            ls.append(word)
        year = ls[5]
        if year != "\N":
            print(year) #year
    else:
        i += 1
