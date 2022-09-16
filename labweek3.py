print('Welcome to the Flarsheim Guesser!')
x = 1
while x == 1:
    print()
    print('Please think of a number between and including 1 and 100.\n')
    r3 = int(input('What is the remainder when your number is divided by 3?'))
    while (r3 >= 3) or (r3 < 0):
        if r3 >= 3:
            print('The value entered must be less than 3')
        else:
            print('The value entered must be 0 or greater')
        r3 = int(input('What is the remainder when your number is divided by 3?'))
    print()
    r5 = int(input('What is the remainder when your number is divided by 5?'))
    while (r5 >= 5) or (r5 < 0):
        if r5 >= 5:
            print('The value entered must be less than 5')
        else:
            print('The value entered must be 0 or greater')
        r5 = int(input('What is the remainder when your number is divided by 5?'))
    print()
    r7 = int(input('What is the remainder when your number is divided by 7?'))
    while (r7 >= 7) or (r7 < 0):
        if r7 >= 7:
            print('The value entered must be less than 7')
        else:
            print('The value entered must be 0 or greater')
        r7 = int(input('What is the remainder when your number is divided by 7?'))
    for num in range(1, 101):
        if (num % 3 == r3) and (num % 5 == r5) and (num % 7 == r7):
           print(f'Your number was {num}')
           print('How amazing is that?\n')
           break
        else:
            continue
    replay = input('Do you want to play again? Y to continue, N to quit ==> ')
    while (replay != 'y') and (replay != 'Y') and (replay != 'n') and (replay != 'N'):
        replay = input('Do you want to play again? Y to continue, N to quit ==> ')
    if (replay == 'n') or (replay == 'N'):
        x = 0
    
