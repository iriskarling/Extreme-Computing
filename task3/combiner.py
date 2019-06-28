#!/usr/bin/env python2
# combiner.py
import sys



act_total = 0

for line in sys.stdin:
    value = int(line)
    act_total += value #count the number for actors and actresses

print(str(act_total))
