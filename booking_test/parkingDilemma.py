import math
import os
import random
import re
import sys

#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#

def carParkingRoof(cars, k):
    # Write your code here
    cars.sort()
    i = 0
    min_cover_length = 0
    while i < len(cars)-k+1:
        current_cover_length = cars[i+k-1] - cars[i] + 1
        if min_cover_length == 0:
            min_cover_length = current_cover_length
        elif min_cover_length > current_cover_length:
            min_cover_length = current_cover_length
        i+=1
    return min_cover_length


if __name__ == '__main__':
    cars_count = int(input().strip())

    cars = []

    for _ in range(cars_count):
        cars_item = int(input().strip())
        cars.append(cars_item)

    k = int(input().strip())

    result = carParkingRoof(cars, k)

    print(str(result) + '\n')