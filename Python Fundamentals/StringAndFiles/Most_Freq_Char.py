s='banana'
l=list(s)
l.sort()
count=1
max=1
max_char=l[0]
for i in range(len(l)-1):
    count=1
    if(l[i]==l[i+1]):
        count+=1
    else:
        count=1
    if(count>max):
        max=count
        max_char=l[i]

print(max_char)


