#!/usr/bin/env python2
# mapper.py
import sys

i = 0
for line in sys.stdin:

    if i>= 1:
        ls =[]
        for word in line.split('\t'):
            ls.append(word)
        if len(ls) == 3:
            id_num = ls[0]
            if ls[1] != "\N":
                attribute = ls[1]
                print(str(id_num)+'\t'+str(attribute)+'\t'+"rating") # tconst/ averageRating /"rating"
        else:
            id_num =ls[0]
            if ls[5] != "\N":
                attribute = ls[5]
                print(str(id_num)+'\t'+str(attribute)+'\t'+"year") #tconst / startYear/"year"
    else:
        i += 1
