def maxInList(l):
    temp=0
    for i in l:
        if(i>temp):
            temp=i
    return temp

l=[23,67,34,56,89]
print(maxInList(l))