#!/usr/bin/env python2
# reducer.py
import sys

vote_num = 0
title_num = 0
avg = 0.00
for line in sys.stdin:
    vote, title= line.strip().split('\t')
    vote_num += float(vote)
    title_num += float(title)
avg = vote_num/title_num #get the average
avg = round(avg,2)
print (str(avg)),
