#!/usr/bin/env python2
# mapper.py
import sys
act_num = 0


for line in sys.stdin:
    # Call map_function for each line in the input
    ls =[]
    for word in line.split('\t'):
        ls.append(word)

    profession = ls[4]
    if "actor" in profession:
        act_num += 1 # count the number for actor
    elif "actress" in profession:
        act_num += 1 #count the number for actress


print(str(act_num))
