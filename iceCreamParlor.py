#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
from collections import Counter


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
# costCount = Counter(cost)
# for i in range(len(cost)):
#     _ = costCount - Counter({cost[i]:1})
#     if money - cost[i] in _:
#         print(i+1, cost[i+1:].index(money-cost[i])+i+2)
#         return
# Too slow... Hmm....

    # costCount = Counter(cost)
    costDict = {}
    for i in range(len(cost)):
        if cost[i] not in costDict:
            costDict[cost[i]] = [i]
        else:
            costDict[cost[i]].append(i)
    # print(costDict)
    for i in range(len(cost)):
        price = cost[i]
        # if money - price in costDict:
        if money - price == price and len(costDict[price]) > 1:
            print(costDict[price][0]+1, costDict[price][1]+1)
            return
        elif money - price != price and money - price in costDict:
            print(costDict[price][0]+1, costDict[money-price][0]+1)
            return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
