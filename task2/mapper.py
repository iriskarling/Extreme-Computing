#!/usr/bin/env python2
# mapper.py
import sys
import string


for line in sys.stdin:
    stro = ''    # Call map_function for each line in the input
    for i in line.strip().split():
        if stro !='' : # stro == ''
            stro = stro + '_' + i  #generate the string
            print(str(stro)+'\t'+'1') #pass the string to the combiner
        stro = i
