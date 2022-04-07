import random

while True:
    gameOptions = ['پشت', 'رو']
    userWins = 0
    computer1Wins = 0
    computer2Wins = 0
    gameCount = 0

    while gameCount < 5:
        userChoice = input('پالام پولوم پیلیش؟(رو یا پشت)')
        computer1Choice = random.choice(gameOptions)
        computer2Choice = random.choice(gameOptions)

        if userChoice in ('پشت', 'رو'):
            print(f'شما: {userChoice}، کامپیوتر1: {computer1Choice}، کامپیوتر2: {computer2Choice}')

            if userChoice == computer1Choice == computer2Choice:
                print(f'مساوی! همه {userChoice} انتخاب کردند')

            else:
                choices = [userChoice, computer1Choice, computer2Choice]
                if choices.count(userChoice) == 1:
                    userWins += 1
                    print('بردی!')

                elif choices.count(computer1Choice) == 1:
                    computer1Wins += 1
                    print('کامپیوتر1 برنده شد!')

                else:
                    computer2Wins += 1
                    print('کامپیوتر2 برنده شد!')

            gameCount += 1
        else:
            print('اشتباه انتخاب کردی دوباره امتحان کن!')

    print('بازی تموم شد ...')
    if (userWins >= computer1Wins) and (userWins >= computer2Wins):
        print('هووورا برنده شدی!!!')
    elif (computer1Wins >= userWins) and (computer1Wins >= computer2Wins):
        print('کامپیوتر1 برنده شد!')
    else:
        print('کامپیوتر2 برنده شد!')

    playAgain = input("بازم بازی کنیم؟ (بله/خیر): ")
    if playAgain == 'خیر':
        break
