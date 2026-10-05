s=input('Enter a String')
#string slicing
print(s[::-1])
#Using for loop
print()
for i in range(s.__len__()-1,-1,-1):
    print(s[i],end="")

