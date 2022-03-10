import math


def add(x, y):
    return round((x + y), 4)


def subtract(x, y):
    return round((x - y), 4)


def multiply(x, y):
    return round((x * y), 4)


def divide(x, y):
    return round((x / y), 4)


def power(x, y):
    return round((x ** y), 4)


def sin(x):
    return round(math.sin(math.radians(x)), 4)


def cos(x):
    return round(math.cos(math.radians(x)), 4)


def tan(x):
    return round(math.tan(math.radians(x)), 4)


def cot(x):
    return round((1 / math.tan(math.radians(x))), 4)


while True:
    calculation = input('عبارت خود را وارد کنید(برای مثال: 2 ^ 2 یا sin(90)): ')
    characters = calculation.split()
    if len(characters) > 1 and characters[1] in ('+', '-', '*', '/', '^'):
        operator = characters[1]
        number1 = float(characters[0])
        number2 = float(characters[2])
        if operator == '+':
            print(number1, operator, number2, '=', add(number1, number2))

        elif operator == '-':
            print(number1, operator, number2, '=', subtract(number1, number2))

        elif operator == '*':
            print(number1, operator, number2, '=', multiply(number1, number2))

        elif operator == '/':
            if number2 == 0:
                print('تعریف نشده!')
            else:
                print(number1, operator, number2, '=', divide(number1, number2))

        elif operator == '^':
            print(number1, operator, number2, '=', power(number1, number2))

    else:
        characters = calculation.split('(')
        if characters[0] in ('sin', 'cos', 'tan', 'cot'):
            operator = characters[0]
            number = float(characters[1].replace(')', ''))
            if operator == 'sin':
                print(operator, '(', number, ')', '=', sin(number))

            elif operator == 'cos':
                print(operator, '(', number, ')', '=', cos(number))

            elif operator == 'tan':
                if number == 90:
                    print('تعریف نشده!')
                else:
                    print(operator, '(', number, ')', '=', tan(number))

            elif operator == 'cot':
                if number == 0:
                    print('تعریف نشده!')
                else:
                    print(operator, '(', number, ')', '=', cot(number))

        else:
            print("ورودی اشتباه است دوباره امتحان کن!")

    nextTry = input("بازم حساب کنیم؟ (بله/خیر): ")
    if nextTry == 'خیر':
        break
