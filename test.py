#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    size = len(arr[0])
    leftrightsum = 0
    rightleftsum = 0
    stop = 0
    line = 0
    column = 0
    
    while stop < size:
        leftrightsum += arr[line][column]
        line += 1
        column += 1
        stop += 1
        
    stop = 0
    line = 0
    column = size-1
    while stop < size:
        rightleftsum += arr[line][column]
        line += 1
        column -= 1
        stop += 1
        
    return abs(leftrightsum - rightleftsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
