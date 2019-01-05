#!/usr/bin/python3

# write a set of random integers up to a
# certain max value to a file `tmp.random'
import random
import sys

try:
    max_lines = sys.argv[1]  # no of random items
except:
    max_lines = 5

ordered = []  # empty list to shuffle

for i in range(max_lines):
    ordered.append(i)

random.shuffle(ordered)

with open("tmp.random", "w+") as f:
    for item in ordered:
        f.writelines("{}\n".format(str(item)))
