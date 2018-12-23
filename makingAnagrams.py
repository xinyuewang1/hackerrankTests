#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    inter = a & b  # intersection
    # print(a.subtract(inter))
    # if inter:
    return sum((a - inter).values()) + sum((b - inter).values())
    # else:
    #     return len(a)+len(b) # no intersection


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)
    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
