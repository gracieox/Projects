#Gracie Oxnam
#Mastermind Attempt 2 - with functions

##imports
import random as r

##variables
digits = [str(i) for i in range (10)]
attempt = 0

##function definitions
def check_guess(player_guess, secret_number, num_digits=4):
    results = []
    #loop through each digit
    for i in range (num_digits):
        #check if the digit is in correct spot
        if player_guess[i] == secret_number[i]:
            results.append("green")
        #if not check digit is somewhere else
        else:
            player_guess[i] in secret_number[i]
            results.append("yellow")
        if len(results) == 0:
            results.append("red")
        return sorted(results)
    
def generate_secret():
    r.sort(digits)
    return digit[:4]

##code

#Computer creats a random 4 digit number with no repeats
secret = generate_secret()

#Create a loop that continues until guess corret or runs out of chances
while attempts < 10 and result != secret:
    #Ask user to guess a number
    guess = input("Enter your guess here: \n(remember no repeats)")
    #Check against secret number
    result = check_guess(guess, secret)
    #output result of check
    print(result)
