########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
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
    if library[5:6] == '1':
        print('School of Computing and Engineering SCE')
    elif library[5:6] == '2':
        print('School of Law')
    elif library[5:6] == '3':
        print('College of Arts and Sciences')
    else:
        print('Invalid School')
        return False
def get_grade(library):
    if library[6:7] == '1':
        print('Freshman')
    elif library[6:7] == '2':
        print('Sophomore')
    elif library[6:7] == '3':
        print('Junior')
    elif library[6:7] == '4':
        print('Senior')
    else:
        print('Invalid Grade')
        return False
def character_value(letter):
    x = string.ascii_uppercase.index(letter)
    return x
def get_check_digit(library):
    sum = 0
    for i in range(0,5):
        x = character_value(library[i])
        sum += x*(i+1)
    for i in range(5,9):
        sum += int(library[i])*(i+1)
    sum = sum%10
    return sum
def verify_check_digit(library):
    if len(library) != 10:
        return False, 'The length of the number given must be 10'
    for i in range(0, 4):
        if library[i].isalpha == False:
            strList = ['The first 5 characters must be A-Z, the invalid character at ', i ,' is ', library[i]]
            str = ''.join(strList)
            return False, str
    for i in range(7,9):
        if library[i].isdigit == False:
            strList = ['The last 3 characters must be 0-9, the invalid character at ', i ,' is ', library[i]]
            str = ''.join(strList)
            return False, str
    if get_school(library) == False:
        return False, 'The sixth character must be 1 2 or 3'
    if get_grade(library) == False:
        return False, 'The seventh character must be 1 2 3 or 4'

    if (get_check_digit(library)) != int(library[9]):
        digList = ['Check digit ', library[9], ' does not match the calculated value of ', get_check_digit(library)]
        dig = ''.join(digList)
        return False, dig
    else:
        return True, ''

            
            

if __name__ == "__main__":

    # main program
    print("Main Program")
    cardNum = input()

        

