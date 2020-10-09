#!/usr/bin/python
import sys
input_str = sys.stdin.read()
lines = input_str.split('\n')
lines.reverse()
for l in lines:
    print(l)
