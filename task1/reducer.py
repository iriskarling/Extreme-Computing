#!/usr/bin/env python2
import sys


word_total = 0
line_total = 0

for line in sys.stdin:
    # Parse key and value
    word_count, line_count = line.strip().split('\t')
    word_total += int(word_count) #count the number for word
    line_total += int(line_count) #count the number for line

print(str(word_total) + '\t' + str(line_total)) # print the final result
