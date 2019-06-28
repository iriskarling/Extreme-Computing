#!/usr/bin/env python2
# reducer.py
import sys



act_total = 0

for line in sys.stdin:
    value = int(line)
    act_total += value #count the number of actors and actresses

print(str(act_total))
