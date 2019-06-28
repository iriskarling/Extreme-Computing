#!/usr/bin/env python2
# mapper.py
import sys
act_num = 0
i = 0


for line in sys.stdin:
    # Call map_function for each line in the input
        ls =[]
        for word in line.strip().split('\t'):
            ls.append(word)
        genre = ls[8].split(',')
        for i in genre:
            if i != "\N":
                print(str(i))
