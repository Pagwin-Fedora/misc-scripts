#!/usr/bin/python
import sys
inp = sys.stdin.read()
sys.stdout.write(inp)
with open(sys.argv[1],'w+') as f:
    f.write(inp)
