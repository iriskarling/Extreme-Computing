#!/usr/bin/env python2
# mapper.py

import sys
line_count = 0 # the number of line
word_count = 0 #the number of word
for line in sys.stdin:
    line_count += 1 #count the number of line
    for word in line.strip().split():
        word_count += 1             #count the number of the count
print(str(word_count) + '\t' + str(line_count)) #pass the value to the combiner 
