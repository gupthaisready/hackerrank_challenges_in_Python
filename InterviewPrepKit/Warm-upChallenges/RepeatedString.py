#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    str_list = list(s)
    str_length = len(str_list)
    a_present_at = []
    a_count_in_s = 0
    
    i=0
    while i < str_length:
        if str_list[i] == 'a':
            a_present_at.append(i)
            a_count_in_s += 1
        i+=1
    
    additional_char_count = n % str_length
    # find a's in additional characters
    addi_char_a_count = 0
    for a_position in a_present_at:
        if a_position+1 <= additional_char_count:
            addi_char_a_count+=1
    
    whole_rep_count = (n-additional_char_count)/str_length
    total_a_count = (a_count_in_s * whole_rep_count) + addi_char_a_count

    return int(total_a_count)



if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')