num=int(input('Enter a number'))
count=0
for i in range(2,num+1):
    count=0
    for j in range(2,i+1):
        if(i%j==0):
                count=count+1

if(count==1):
    print('Prime number')
else:
    print('Not prime')

    
