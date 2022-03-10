while True:
    print('ضلع ها را یک به یک وارد کنید:')

    a = []

    for i in range(3):
        el = int(input())

        a.append(el)

    if a[0] + a[1] > a[2] and a[0] + a[2] > a[1] and a[1] + a[2] > a[0]:
        print('مثلث تشکیل میشه')
    else:
        print('مثلث تشکیل نمیشه!')

    nextTry = input("بازم امتحان کنیم؟ (بله/خیر): ")
    if nextTry == 'خیر':
        break
