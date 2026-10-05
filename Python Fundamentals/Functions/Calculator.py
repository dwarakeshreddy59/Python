def calculator(a,b,operator):
    match operator:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '*':
            print(a*b)
        case '/':
            print(a/b)
        case '%':
            print(a%b)
        case _:
            print('Invalid operator')

calculator(99,21,'+')