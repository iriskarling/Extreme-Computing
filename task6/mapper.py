#!/usr/bin/env python2
# mapper.py
import sys

i = 0
vote_num = 0
title_num = 0
for line in sys.stdin:
    title_num += 1
    if i >= 1:
        ls =[]
        for word in line.split('\t'):
            ls.append(word)
        vote_num += int(ls[2]) # get the number of vote

    else:
        i += 1
print(str(vote_num)+'\t'+str(title_num))
