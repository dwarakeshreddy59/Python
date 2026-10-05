# s=input('Enter a string')
s='Pagani'
s2=''
j=0
for i in range(len(s)-1,-1,-1):
    # print(s[i])
    s2+=s[i]
    j+=1
print(s)
print(s2)