#!/bin/python3

from ctypes import pointer
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if i >= 1:
            positive+=1
        elif i < 0:
            negative+=1
        elif i == 0:
            zeros+=1

    print(format(positive/len(arr),'.6f'))
    print(format(negative/len(arr),'.6f'))
    print(format(zeros/len(arr),'.6f'))


if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    plusMinus([1,1,0,-1,-1])
