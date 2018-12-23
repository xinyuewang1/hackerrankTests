#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    arrCounter = Counter(arr)
    triplet = 0
    print(arrCounter)
    for key, value in arrCounter.items():
        if key == 1 and r == 1:
            print("return 1")
            return math.factorial(value)/(math.factorial(3)*math.factorial(value-3))
        if key*r in arrCounter and key*r*r in arrCounter:
            triplet += value*arrCounter[key*r]*arrCounter[key*r*r]
    return triplet

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()
