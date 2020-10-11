#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    path_list = list(path)
    print (path_list)
    currently_at = 0 # denotes valley, positive is mountain & negative is valley
    valley_count = {}
    valley_num = 0
    result = 0
    for each_path in path_list:
        if each_path == 'U':
            currently_at += 1
            if currently_at == 0:
                valley_count[valley_num] = 'End'
        elif each_path == 'D':
            if currently_at == 0:
                valley_num += 1
                valley_count.setdefault(valley_num, 0)
                valley_count[valley_num] = 'Begin'
            currently_at -= 1
        print (currently_at, valley_count, valley_num)
    for valley_key, valley_val in valley_count.items():
        if valley_val == 'End':
            result += 1
    return result


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(str(result) + '\n')