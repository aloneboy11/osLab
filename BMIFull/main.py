while True:
    weight = int(input('وزن: '))
    height = int(input('قد: '))

    bmi = (weight / (height ** 2)) * 10000

    if bmi < 18.5:
        print('لاغر')

    elif 18.5 <= bmi < 25:
        print('عادی')

    elif 25 <= bmi < 30:
        print('توپر')

    elif 30 <= bmi < 35:
        print('چاق')

    elif 35 <= bmi:
        print('خرس')

    nextTry = input("بازم حساب کنیم؟ (بله/خیر): ")
    if nextTry == 'خیر':
        break
