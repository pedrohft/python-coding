#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[0:4])
    max_sum = sum(sorted_arr[1:])

    print(f'{min_sum} {max_sum}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
