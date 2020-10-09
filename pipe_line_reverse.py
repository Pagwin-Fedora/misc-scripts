#!/usr/bin/python
#redundant because I know tac exists but at the time I was unaware of that
import sys
input_str = sys.stdin.read()
lines = input_str.split('\n')
lines.reverse()
for l in lines:
    print(l)
