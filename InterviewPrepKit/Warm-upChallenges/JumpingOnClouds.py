#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    count = 0
    while i < len(c)-2:
        i= i+1 if c[i+2] else i+2
        count+=1
    if i == len(c)-2: # it has one more cloud to hop to
        count+=1

    return count

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')