a=int(input('Pick a car from below menu'))
match a:
    case 1:
        print('Ferrari 296 challenge')
    case 2:
        print('Ferrari pista')
    case 3:
        print('Porche gt3 RS')
    case 4:
        print('Benz Black series')
    case 5:
        print('Aston Martin Vallhalla')
    case _:
        print('Enter correct option')