#!/usr/bin/env python2
# mapperb.py
import sys


for line in sys.stdin:
    year,rating= line.strip().split('\t')
    if int(year)< 2010 and  int(year) >= 1900:
        t = (int(year)-1900)/10
        t = 1900 + t*10 # preprocess the year into the format of decade
        print(str(t)+'\t'+str(rating)) # decade /averageRating
