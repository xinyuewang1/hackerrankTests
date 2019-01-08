#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    # sorted
    # calculate the gap
    # sort
    # pick first kth and sum the gap
    # arr = sorted(arr)
    # print(arr)
    # gap = []
    # for i in range(1, len(arr)):
    #     gap.append(arr[i] - arr[i-1])
    # print(gap)
    # minGap = sum(gap[:k-1])
    # for i in range(k, len(gap)):
    #     # print(i, k)
    #     _ = sum(gap[i-k+1:i])
    #     if _ < minGap:
    #         minGap = _
    # return minGap

    # timeout, second try
#     Hmm, the find gap could be removed
    arr = sorted(arr)
    minGap = arr[k-1] - arr[0]
    for i in range(k, len(arr)):
        _ = arr[i] - arr[i-k+1]
        if _ < minGap:
            minGap = _
    return minGap


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
