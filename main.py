def calc():
    print('''
    Welcome to the calculator program
    ''')
    
    operation = input('''
    Enter the operation you want to perform:'
    '+' for addition
    '-' for subtraction'
    '*' for multiplication'
    '/' for division''
    ''')
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)
    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)
    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)
    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)
    else:
        print('You have entered an invalid operator')
calc()
def calc_again():
    calc_again1 = input('''
    Do you want to calculate again?
    Y for yes
    N for no
    ''')
    if calc_again1.upper() == 'Y':
        calc()
    elif calc_again1.upper() == 'N':
        print('See you later')
    else:
        calc_again()
