#!/bin/python3

import math
import os
import random
import re
import sys

def min_time(roads, machines):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    num_cities, num_machines = map(int, input().split())

    roads = []
    for _ in range(num_cities - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = [] # these are cities machines are in
    for _ in range(num_machines):
        machines.append(int(input()))

    result = min_time(roads, machines)

    fptr.write(str(result) + '\n')
    fptr.close()