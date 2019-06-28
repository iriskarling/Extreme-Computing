#!/usr/bin/env python2
# combiner.py
import sys

vote_num = 0
title_num = 0
avg = 0.00
for line in sys.stdin:
    vote, title= line.strip().split('\t')
    vote_num += float(vote) #count the number of vote
    title_num += float(title) #count the number of title

print(str(vote_num)+'\t'+str(title_num))  #get the number of vote and the number of title
