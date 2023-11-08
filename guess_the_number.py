import random

logo = '''
   ____                                              __________ ___                      ___      ___                         ___                       
  6MMMMb/                                            MMMMMMMMMM `MM                      `MM\\     `M'                          MM                       
 8P    YM                                            /   MM   \\  MM                       MMM\\     M                           MM                       
6M      Y ___   ___   ____     ____     ____             MM      MM  __     ____          M\\MM\\    M ___   ___ ___  __    __   MM____     ____  ___  __ 
MM        `MM    MM  6MMMMb   6MMMMb\\  6MMMMb\\           MM      MM 6MMb   6MMMMb         M \\MM\\   M `MM    MM `MM 6MMb  6MMb  MMMMMMb   6MMMMb `MM 6MM 
MM         MM    MM 6M'  `Mb MM'    ` MM'    `           MM      MMM9 `Mb 6M'  `Mb        M  \\MM\\  M  MM    MM  MM69 `MM69 `Mb MM'  `Mb 6M'  `Mb MM69 " 
MM     ___ MM    MM MM    MM YM.      YM.                MM      MM'   MM MM    MM        M   \\MM\\ M  MM    MM  MM'   MM'   MM MM    MM MM    MM MM'    
MM     `M' MM    MM MMMMMMMM  YMMMMb   YMMMMb            MM      MM    MM MMMMMMMM        M    \\MM\\M  MM    MM  MM    MM    MM MM    MM MMMMMMMM MM     
YM      M  MM    MM MM            `Mb      `Mb           MM      MM    MM MM              M     \\MMM  MM    MM  MM    MM    MM MM    MM MM       MM     
 8b    d9  YM.   MM YM    d9 L    ,MM L    ,MM           MM      MM    MM YM    d9        M      \\MM  YM.   MM  MM    MM    MM MM.  ,M9 YM    d9 MM     
  YMMMM9    YMMM9MM_ YMMMM9  MYMMMM9  MYMMMM9           _MM_    _MM_  _MM_ YMMMM9        _M_      \\M   YMMM9MM__MM_  _MM_  _MM_MYMMMM9   YMMMM9 _MM_    
'''

print(logo)

choice = input('Do you wanna play, "Guess the number? y or n : ').lower()

while choice == 'y':

    def guessed_number(guess, num, lives):
        if guess > num:
            print('Number too big, guess again...')
            return lives, False
        elif guess < num:
            print('Number too small, guess again...')
            return lives, False
        else:
            print("Yes, you guessed it correct. The number is " + str(guess))
            return 0, True

    num = random.randint(0, 100)
    level = input("What level you want to play: 'easy' or 'hard' ")

    if level == 'easy':
        print('You chose easy. you have 10 attempts.')
        lives = 10
    else:
        print('You chose hard, you have 5 attempts')
        lives = 5

    while lives > 0:
        guess = int(input('Guess the number (It\'s between 1 and 100) : '))
        lives, won = guessed_number(guess, num, lives)
        lives -= 1

    if won:
        print('You Win')
    else:
        print('You lose.')

    choice = input('You wanna play again? y or n : ')

print('Thanks for playing.')
