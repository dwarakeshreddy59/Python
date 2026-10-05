num=153
num2=num
# count=0
# for i in num:
#     count=count+1
#     print(i)

# print(count)
# print(len(str(num)))
# WHile Loop for count the length
count=0
while(num>0):
    num=num//10
    count=count+1

# print(count)

# for calculation
sum=0
while(num2>0):
    digit=num2%10
    sum=sum+digit**count
    num2=num2//10
    

print(sum)
