#gracie oxnam
#rock paper scissors
#string practice

import random as r

player1_wins = 0
player2_wins = 0

options = ["rock", "paper", "scissors"]
#player1 = (r.choice (options))
#player2 = (r.choice (options))

def player_choice(player_type):
    if player_type == "c":
        player_choice = r.choice(options)
    else:
        player_choice = input("enter your choice here: ")

player1 = player_choice ("h")
player2 = player_choice("c")
    
def test_rps (player1, player2):
    options = ["rock", "paper", "scissors"]
    print (player1, player2)
    if player1 == player2:
        return ("tie")
    if ('rock', 'paper') or ('paper', 'scissors') or ('scissors', 'rock'):
        return ("player 2")
        player1_wins
    if ('paper', 'rock') or ('scissors', 'paper') or ('rock', 'scissors'):
        return ("player 1")

test_rps(player1, player2)
