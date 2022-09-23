########################################################################
##
## CS 101 Lab
## Program #4
## Name Patrick Rogan
## Email pjrh9f@umsystem.edu
##
## PROBLEM : There is code for a slots game, but the functions in the code need to be completed
##
## ALGORITHM : 
##      1. Ask the user for a starting bank
##      2. Ask the user for a starting wager
##      3. Spin for 3 random numbers, then check for matches
##      4. Either reward chips or take away chips, depending on the number of matches
##      5. If the user still has chips in their bank, keep playing.
##      6. If the user has no more chips, ask them if they want to keep playing.
##      7. If the user wants to keep playing, repeat the previous steps.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    replay = input('Do you want to play again? ==> ')
    replay = replay.upper() #turns all inputs into uppercase
    while (replay != 'N') and (replay != 'NO') and (replay != 'Y') and (replay != 'YES'):
        print()
        print('You must enter Y/YES/N/NO to continue. Please try again') #invalid input line
        replay = input('Do you want to play again? ==> ')
        replay = replay.upper()
    if (replay == 'N') or (replay == 'NO'): #user doesn't want to play again
        return False
    else:  #user wants to play again
        return True
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    x = 0
    while x == 0:
        wager = int(input('How many chips do you want to wager? ==> '))
        if (wager > bank):  #checks if the wager amount is greater than the total bank
            print(f'The wager amount cannot be greater than how much you have. {bank}')
        elif (wager < 0):  #checks if the wager is negative
            print('The wager amount must be greater than 0. Please enter again.')
        else:
            x = 1
    return wager            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    rand1 = random.randint(1,10)  #gets the first random integer
    rand2 = random.randint(1,10)  #gets the second random integer
    rand3 = random.randint(1,10)  #gets the third random integer

    return rand1, rand2, rand3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc:  #checks if all 3 reels match
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):  #checks if 2 reels match
        return 2
    else:  #no reels match
          return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    x = 0
    while x == 0:
        bank = int(input('How many chips do you want to start with? ==> '))
        if bank <= 0:  #checks if bank is a negative number
            print('Too low a value, you can only choose 1 - 100 chips')
        elif bank > 100:  #checks if bank is over 100
            print('Too high a value, you can only choose 1 - 100 chips')
        else:
            x = 1
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:  #multiplies the wager by 10 if there are 3 matches
        return wager * 10
    elif matches == 2:  # triples the wager if there are 2 matches
        return wager * 3
    else:  #turns the wager into a negative if no matches are found
        return wager * -1     


if __name__ == "__main__":

    playing = True
    totalSpins = 0
    while playing:

        bank = get_bank()
        start = bank  #stores the starting value in its own variable
        maxBank = bank  #starts the maxBank value with the starting bank value

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            totalSpins += 1 #increments up 1 everytime a spin happens
            if bank > maxBank:  #checks if the current bank is higher than the max
                maxBank = bank
           
        print("You lost all", start, "in", totalSpins, "spins")
        print("The most chips you had was", maxBank)
        playing = play_again()
