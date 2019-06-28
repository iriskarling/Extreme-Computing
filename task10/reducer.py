#!/usr/bin/env python2
# reducer.py
import sys


prev_key = None
prev_attribute = None
prev_type = None
check = False #for check if there is a type(year) before the following same type(crew)

for line in sys.stdin:
    id_num,attribute,ty = line.strip().split('\t') # tconst, year/nconst, type
    if ty == "year":
        check = True
    elif (check):
        if id_num == prev_key :
            if ty == "crew":
                print(str(attribute)) #ensure that the nconst would be printed

        elif id_num !=prev_key :
            check = False 
    prev_key = id_num
    prev_attribute = attribute
    prev_type = ty
