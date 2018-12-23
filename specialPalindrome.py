#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
from collections import Counter


# def isSpecialPalindrome (s):
#     sC = Counter(s)
#     if len(sC) == 1:
#         return True
#     elif len(sC) == 2 and len(s) > 2 and sC[s[len(s)//2]] == 1:
#         return True
#     return False
#
#
# # Complete the substrCount function below.
# def substrCount(n, s):
#     count = n
#     # count = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if isSpecialPalindrome(s[i:j+1]):
#                 print(s[i:j+1])
#                 count += 1
#     return count


def substrCount (n, s):
    # sC = Counter(s)
    for i in range(n):


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 5
    # s = input()
    s = "asasd"
    result = substrCount(n, s)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
