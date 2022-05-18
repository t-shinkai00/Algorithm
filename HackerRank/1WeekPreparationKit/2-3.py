#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = [0 for i in range(100)]
    for el in arr:
        result[el] += 1
    return result

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    result = countingSort(arr)

    print(result)
