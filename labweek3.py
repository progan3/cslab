print('Welcome to the Flarsheim Guesser!')
x = 1 #this variable is used to keep my loop infinite until the user wants to stop
while x == 1:
    print()
    print('Please think of a number between and including 1 and 100.\n')
    r3 = int(input('What is the remainder when your number is divided by 3?'))
    while (r3 >= 3) or (r3 < 0): #this while loop checks if the input is greater or equal to 3 or a negative number
        if r3 >= 3:
            print('The value entered must be less than 3') #prints if input is greater or equal to 3
        else:
            print('The value entered must be 0 or greater') #prints if input is negative
        r3 = int(input('What is the remainder when your number is divided by 3?'))
    print()
    r5 = int(input('What is the remainder when your number is divided by 5?'))
    while (r5 >= 5) or (r5 < 0): #this while loop checks if the input is greater or equal to 5 or a negative number
        if r5 >= 5:
            print('The value entered must be less than 5') #prints if input is greater or equal to 5
        else:
            print('The value entered must be 0 or greater') #prints if input is negative
        r5 = int(input('What is the remainder when your number is divided by 5?'))
    print()
    r7 = int(input('What is the remainder when your number is divided by 7?'))
    while (r7 >= 7) or (r7 < 0): #this while loop checks if the input is greater or equal to 7 or a negative number
        if r7 >= 7:
            print('The value entered must be less than 7') #prints if input is greater or equal to 7
        else:
            print('The value entered must be 0 or greater') #prints if input is negative
        r7 = int(input('What is the remainder when your number is divided by 7?'))
    for num in range(1, 101): #iterates through a range of all numbers between 1 and 100
        if (num % 3 == r3) and (num % 5 == r5) and (num % 7 == r7): #checks the remainder of each number
           print(f'Your number was {num}') #prints the guessed number
           print('How amazing is that?\n')
           break #ends the for loop
        else:
            continue
    replay = input('Do you want to play again? Y to continue, N to quit ==> ') #asks user if they want to play again
    while (replay != 'y') and (replay != 'Y') and (replay != 'n') and (replay != 'N'): #loop used on inputs that won't work
        replay = input('Do you want to play again? Y to continue, N to quit ==> ')
    if (replay == 'n') or (replay == 'N'): #checks if the user wants to stop playing
        x = 0 #ends the while loop
    
