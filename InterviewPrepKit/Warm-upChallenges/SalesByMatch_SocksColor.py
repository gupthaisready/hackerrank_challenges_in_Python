import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total_pairs = 0
    colors = {}
    for col_num in ar:
        colors.setdefault(col_num, 0)
        colors[col_num] += 1
    for each_color, color_total in colors.items():
        if color_total % 2 == 0:
            total_pairs += color_total/2
        else:
            total_pairs += (color_total-1)/2
    return int(total_pairs)

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
