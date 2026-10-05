def largest_num(a,b,c):
    if(a>b and a>c):
        return 'A is great'
    elif(b>a and b>c):
        return 'B is great'
    else:
        return 'C is great'

print(largest_num(23,67,10))