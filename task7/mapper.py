#!/usr/bin/env python2
# mapper.py
import sys

i = 0
writer_num = 0
title_num = 0
for line in sys.stdin:
    # Call map_function for each line in the input
    title_num += 1
    if i >= 1:
        ls =[]
        for word in line.split('\t'):
            ls.append(word)
        if ls[2] != "\N":
            writer = ls[2].split(',')
            writer_num += len(writer)
        if ls[2] == "\N":
            title_num -=1 #if the person don't have the title, the number of title need change
    else:
        i += 1
print(str(writer_num)+'\t'+str(title_num))
