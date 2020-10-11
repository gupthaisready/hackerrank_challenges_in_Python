import math
import os
import random
import re
import sys



#
# Complete the 'countDuplicate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countDuplicate(numbers):
    # Write your code here
    duplicate_counter = {}
    for num in numbers:
        duplicate_counter.setdefault(num, 0)
        duplicate_counter[num] += 1
    total_duplicates = 0
    for dup_key, dup_val in duplicate_counter.items():
        if dup_val > 1:
            total_duplicates += 1
    return total_duplicates

if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = countDuplicate(numbers)

    print(str(result) + '\n')