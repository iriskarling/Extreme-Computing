#!/usr/bin/env python2
# reducer.py
import sys

writer_num = 0
title_num = 0
avg = 0.00
for line in sys.stdin:
    # Parse key and value
    writer, title= line.strip().split('\t')
    writer_num += float(writer)
    title_num += float(title)
avg = writer_num/title_num
avg = round(avg)
avg = int(avg)
print (str(avg)), #print the average 
