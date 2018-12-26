#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from collections import Counter


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
    # idea from discussion, it's "Compression" idea. Very neat.
    if n != 0:
        count = 1
        tmp = s[0]
        l = [[tmp, 1]]

        for i in range(1, n):
            if s[i] == tmp:
                l[-1][1] += 1  # add one when it's the same char

            else:
                tmp = s[i]
                l.append([tmp, 1])
            count += l[-1][1]
        # print(l)

        for x in range(1, len(l)-1):
            if l[x-1][0] == l[x+1][0] and l[x][1] == 1:
                count += min(l[x-1][1], l[x+1][1])

        return count
    else:
        return "Error"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 5
    # s = input()
    s = "aasasd"
    result = substrCount(n, s)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
