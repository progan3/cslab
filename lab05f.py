########################################################################
##
## CS 101 Lab
## Program #5
## Name Patrick Rogan
## Email pjrh9f@umsystem.edu
##
## PROBLEM : We are asking users for a library card and checking if it is valid or invalid.
##
## ALGORITHM : 
##      1. Ask the user for a card number
##      2. If the card is invalid, print that the card is invalid and why
##      3. If the card is valid, print that the card is valid, the cardholder's school, and grade.
##      4. Ask the user for another card number, end the program if the user hits enter
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements
import string
# functions
def get_school(library):
    if library[5:6] == '1': #checks if 6th value is 1
        return 'School of Computing and Engineering SCE'
    elif library[5:6] == '2':  #checks if 6th value is 2
        return 'School of Law'
    elif library[5:6] == '3':  #checks if 6th value is 3
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
        return False
def get_grade(library):
    if library[6:7] == '1': #checks if 7th value is 1
        return 'Freshman'
    elif library[6:7] == '2':  #checks if 7th value is 2
        return 'Sophomore'
    elif library[6:7] == '3':  #checks if 7th value is 3
        return 'Junior'
    elif library[6:7] == '4':  #checks if 7th value is 4
        return 'Senior'
    else:
        return 'Invalid Grade'
        return False
def character_value(letter):
    x = string.ascii_uppercase.index(letter)  
    return x  #prints the value of a string
def get_check_digit(library):
    sum = 0
    for i in range(0,5):  #goes through the 1st - 5th values
        x = character_value(library[i])
        sum += x*(i+1)
    for i in range(5,9):  #goes through the 6th - 9th values
        sum += int(library[i])*(i+1)
    sum = sum%10  
    return sum
def verify_check_digit(library):
    if len(library) != 10:  #checks length of the input
        return False, 'The length of the number given must be 10'
    for i in range(0, 5):
        if library[i].isalpha() == False:  
            return False, 'The first 5 characters must be A-Z, the invalid character at {} is {}'.format(i, library[i])  #returns if one of the first 5 values is not a letter
    for i in range(7,9):
        if library[i].isdigit() == False:
            return False, 'The last 3 characters must be 0-9, the invalid character at {} is {}'.format(i, library[i])  #returns if one of the end values is not a number
    if get_school(library) == False:
        return False, 'The sixth character must be 1 2 or 3'  #checks if the user has a valid school
    if get_grade(library) == False:
        return False, 'The seventh character must be 1 2 3 or 4'  #checks if the user has a valid grade

    if (get_check_digit(library)) != int(library[9]):  #checks the check digit
        return False, 'Check digit {} does not match the calculated value of {}'.format(library[9], get_check_digit(library))  
    else:
        return True, ''  #returns when the input is valid

            
            

if __name__ == "__main__":

    # main program
    print("Main Program")
    text1 = 'Linda Hall'
    text2 = 'Library Card Check'
    new_str = text1.center(70) #centers text1 on the screen
    new_str2 = text2.center(70) #centers text2 on the screen
    print(new_str)
    print(new_str2)
    print('='*80)
    while True:
        print()
        cardNum = input('Enter Library Card. Hit Enter to Exit ==> ')
        if not cardNum:
            break #ends the loop if the user hits enter
        if verify_check_digit(cardNum)[0] == False:
            print('Library card is invalid.')
            print(verify_check_digit(cardNum)[1]) #prints why the card is invalid
        elif verify_check_digit(cardNum)[0] == True:
            print('Library card is valid.')
            print(f'This card belongs to a student in {get_school(cardNum)}') #prints the school of the card holder
            print(f'This card belongs to a {get_grade(cardNum)}') #prints the grade of the card holder


        

