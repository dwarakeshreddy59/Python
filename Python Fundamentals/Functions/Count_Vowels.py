def Count_Vowels(s):
    count=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            count+=1

    return count

print(Count_Vowels('Ferrari'))