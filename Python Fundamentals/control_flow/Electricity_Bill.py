unit=int(input('Enter the units'))
if(unit>0 and unit<=100):
    print('2 rs per unit')
elif(unit>100 and unit<=200):
    print('3 rs per unit')
else:
    print('5 rs per unit')