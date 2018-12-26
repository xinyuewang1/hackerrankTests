#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
import numpy as np

# Complete the commonChild function below.
# def commonChild(s1, s2):
    # first thought: child could only be in intersection chars.
    # charSet = set(list(s1)).intersection(set(list(s2)))
    # # print(charSet)
    # for char in s1:
    #     # print(char)
    #     if char not in charSet:
    #         # print("remove")
    #         s1 = s1.replace(char, "")
    # for char in s2:
    #     if char not in charSet:
    #         s2 = s2.replace(char, "")
    # print(s1, s2)
    # if s1 == s2:
    #     return len(s1)
    # else:
    #     children = []
    #     base = s1
    #     compare = s2
    #     if len(s1) > len(s2):
    #         base = s2
    #         compare = s1
    #     # use the shorter list as base
    #     for i in range(len(base)):
    #         for j in range(len(compare)):
    #             if base[i] == compare[j]:
    #                 # print(children)
    #                 for child in children:
    #                     # print(children)
    #                     if j > child[-1][1] and compare[j] != child[-1][0]:
    #                         # print(children)
    #                         # print("INside",child.append(j))
    #                         children.append(child)  # keep possibility open
    #                         child.append((compare[j], j))
    #                         # HNHAN
    #                         # NHAAAA
    #
    #                         # print(children)
    #                 # print(children)
    #                 # print("outside",[j])
    #                 children.append([(compare[j], j)])
    #     length = 0
    #     for child in children:
    #         if len(child) > length:
    #             length = len(child)
    #
    #     return length

# Pseudocode from wiki: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# function LCSLength(X[1..m], Y[1..n])
#     C = array(0..m, 0..n)
#     for i := 0..m
#        C[i,0] = 0
#     for j := 0..n
#        C[0,j] = 0
#     for i := 1..m
#         for j := 1..n
#             if X[i] = Y[j]
#                 C[i,j] := C[i-1,j-1] + 1
#             else
#                 C[i,j] := max(C[i,j-1], C[i-1,j])
#     return C[m,n]


def commonChild(s1, s2):
    charSet = set(list(s1)).intersection(set(list(s2)))
    # print(charSet)
    for char in s1:
        # print(char)
        if char not in charSet:
            # print("remove")
            s1 = s1.replace(char, "")
    for char in s2:
        if char not in charSet:
            s2 = s2.replace(char, "")

    # print(s1, s2)

    m, n = len(s1), len(s2)
    matrix = np.zeros(shape=(m+1, n+1))
    # print(matrix)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrix[i, j] = matrix[i-1, j-1] + 1
            else:
                matrix[i, j] = max(matrix[i, j-1], matrix[i-1, j])
    print(matrix)
    return np.amax(matrix)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s1 = input()
    #
    # s2 = input()
    s1 = "HARRY"
    s2 = "SALLY"

    result = commonChild(s1, s2)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
