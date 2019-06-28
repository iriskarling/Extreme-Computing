#!/usr/bin/env python2
# mapper.py
import sys


year = 0
for line in sys.stdin:
    # Call map_function for each line in the input
        ls =[]
        for word in line.strip().split('\t'):
            ls.append(word)
        if ls[5] != "\N":
            year = ls[5]
            if ls[8] != "\N":
                genres = ls[8].strip().split(',')
                for g in genres:
                    if g != "\N":
                        print(str(g)+'\t'+str(year)) # genres /year
