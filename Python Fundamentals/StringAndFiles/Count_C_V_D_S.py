#Count Vowels, Consonants, Digits, and Spaces
s=input('Enter a string')
s.lower()

#Loop for vowels
vcount=0
ccount=0
dcount=0
scount=0
for i in s:
    if(i =='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vcount+=1
    elif('0'<=i<='9'):
        dcount+=1
    elif('a'<=i<='z'):
        ccount+=1
    elif(i==' '):
        scount+=1


print('Vowels count =',vcount)
print('Consonants count=',ccount)
print("Digits count=",dcount)
print('Space count=',scount)





