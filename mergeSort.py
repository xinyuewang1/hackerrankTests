#!/bin/python3

# import math
import os
# import random
# import re
# import sys
# from collections import deque

class MergeSort:
    inver = 0

    def merge(self, a, b):
        # global inver
        s = []
        # a, b = deque(a), deque(b)
        # while a and b:
        len_a, len_b = len(a), len(b)
        i_a , i_b = 0, 0
        # for i in range(min(len_a, len_b)):
        while i_a < len_a and i_b < len_b:
            # print("a, b:", a, b)
            # if a[0] <= b[0]:
                # s.append(a.popleft())
                # s.append(a[0])
                # del a[0]
                # s.append(a.pop(0))
            if a[i_a] <= b[i_b]:
                # s.append(a[i])
                s.append(a[i_a])
                # len_a -= 1
                i_a += 1
            else:
                # s.append(b.popleft())
                # s.append(b[0])
                # del b[0]
                # s.append(b.pop(0))
                s.append(b[i_b])
                i_b += 1
                # print(len(a))
                print("inver before:", self.inver)
                print(a, b)
                print(len_a, i_a)
                self.inver += len_a - i_a
                print("inver after:", self.inver)
                # print(inver)
        # a, b = list(a), list(b)
        if i_a < len_a:
            s += a[i_a:]
        if i_b < len_b:
            s += b[i_b:]

        # print(s)
        return s

    def mergeSort(self, arr):
        length = len(arr)
        if length < 2:
            return arr
        mid = length // 2
        s1, s2 = arr[:mid], arr[mid:]
        s1 = self.mergeSort(s1)
        s2 = self.mergeSort(s2)
        # print("Arr", arr, "s1", s1, "s2", s2)
        return self.merge(s1, s2)

    def getInver(self):
        return self.inver

# Complete the countInversions function below.
def countInversions(arr):
    # naive approach bigO(n^2)
    # swap = 0
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] > arr[j]:
    #             swap += 1
    # return swap

    # I was wondering why this is called "merge sort", and then I realized how to merge.
    # It seems like using merge sort and when merge, count the swap
    # MergeSort, should be O(nlogn)
    # global inver
    # arr = deque(arr)
    x = MergeSort()
    x.mergeSort(arr)
    # print(inver)
    return x.getInver()



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
