#!/usr/bin/env python2
# combiner.py
import sys

writer_num = 0
title_num = 0
avg = 0.00
for line in sys.stdin:
    # Parse key and value
    writer, title= line.strip().split('\t')
    writer_num += float(writer)
    title_num += float(title)

print(str(writer_num)+'\t'+str(title_num)) #the number of writer and the number of title
