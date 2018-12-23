#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from statistics import median


def findMax(array):
    temp = array[0]
    for i in range(1, len(array)):
        if temp < array[i]:
            temp = array[i]
    return temp

def getCounting(array):
    # print("Array",array)
    # This will be space efficient but extra step to find Max. However, it shall fast counting sort step
    x = [0] * (findMax(array) + 1)  # extra space for 0 at the beginning
    # y = [0] * len(x)
    # print(len(x), len(y))
    for a in array:
        x[a] += 1
        # y[a] += 1
    # y = [0] * len(x)
    # print(x, y)
    # for _ in range(1, len(x)):
    #     y[_] += y[_ - 1]
    # print(x, y)
    # x is counting, y is incrementing counting

def findMedian(x, length):

    if length % 2 == 0:
        medianPos1 = length // 2  # if length is 6, median is avg of pos3 and pos4
        medianPos2 = medianPos1 + 1
        med1 = 0
        med2 = 0
        for i in range(len(x)):
            med1 += x[i]
            # if y[i] >= medianPos1:
            if med1 >= medianPos1:
                med1 = i
                break

        for i in range(len(x)):
            med2 += x[i]
            if med2 >= medianPos2:
                med2 = i
                break

        return (med1 + med2) / 2

    if length % 2 == 1:
        medianPos = length // 2 + 1
        # print(medianPos)
        med = 0
        for i in range(0, len(x)):
            med += x[i]
            if med >= medianPos:
                return i


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notice = 0
    window = expenditure[:d]
    # x = [0] * (findMax(expenditure) + 1)  # extra space for 0 at the beginning
    x = [0] * 201
    for a in window:
        x[a] += 1

    for i in range(d, len(expenditure)):
        # print(expenditure[i], findMedian(expenditure[i - d:i]))
        if expenditure[i] >= findMedian(x, d) * 2:
            notice += 1
    #     slide window
        x[expenditure[i-d]] -= 1
        x[expenditure[i]] += 1
    return notice
    # time out

# def activityNotifications(expenditure, d):


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
