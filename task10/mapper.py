#!/usr/bin/env python2
# mapper.py
import sys


for line in sys.stdin:
        ls =[]
        for word in line.split('\t'):
            ls.append(word)
        if len(ls) == 6:
            id_num = ls[0]
            if ls[5] != "\N":
                attribute = ls[5].strip().split(',')
                for a in attribute:
                    print(str(a)+'\t'+str(id_num)+'\t'+"crew") # tconst/ nconst/ "crew"

        else:
            tid_num =ls[0]
            if ls[5] != "\N":
                attribute = ls[5]
                if int(attribute)>= 2010 and int(attribute)<=2018:
                    print(str(tid_num)+'\t'+str(attribute)+'\t'+"year") # tconst/year/"year"
