list of integer
return max integer
def function maxInt(l) :
    if len(l) == 0:
        return -1
    tmp = l[0]
    for i in range(1,len(l)):
        if l[i] > tmp:
            tmp = l[i]

    return tmp

