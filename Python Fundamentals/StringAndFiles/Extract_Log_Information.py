s="2026-10-05 10:15:20 ERROR Database connection failed"
p=s.split()
print(p)
print('Timestamp:',p[0],p[1])
print('Level:',p[2])
print('Message:',p[3],p[4],p[5])