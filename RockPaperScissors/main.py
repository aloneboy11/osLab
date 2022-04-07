import random

while True:
    userChoice = input('سنگ، کاغذ، قیچی؟')
    gameOptions = ['سنگ', 'کاغذ', 'قیچی']
    computerChoice = random.choice(gameOptions)

    if userChoice == computerChoice:
        print(f'مساوی! هردو {userChoice} را انتخاب کردید.')

    elif userChoice == 'سنگ':
        if computerChoice == 'کاغذ':
            print('باختی! کاغذ سنگ رو میپوشونه.')
        else:
            print('بردی! سنگ قیچی رو میشکونه.')

    elif userChoice == 'کاغذ':
        if computerChoice == 'سنگ':
            print('بردی! کاغذ سنگ رو میپوشونه.')
        else:
            print('باختی! قیچی کاغذ رو میبره.')

    elif userChoice == 'قیچی':
        if computerChoice == 'سنگ':
            print('باختی! سنگ قیچی رو میشکونه.')
        else:
            print('بردی! قیچی کاغذ رو میبره.')

    else:
        print('اشتباه انتخاب کردی دوباره امتحان کن!')

    playAgain = input("بازم بازی کنیم؟ (بله/خیر): ")
    if playAgain == 'خیر':
        break
