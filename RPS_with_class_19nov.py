#gracie oxnam
#rock paper scissors WITH CLASS

import random as r
options = ["r", "p", "s"]

def test_rps (player1, player2):
    if player1 == "rock":
        if player2 [0] == "s":
            return "player 1"
        elif player2 [0] == "p":
            return "player 2"
        else:
            return "tie"
    if player1 == "scissors":
        if player2 [0] == "p":
            return "player 1"
        elif player2 [0] == "r":
            return "player 2"
        else:
            return "tie"
    if player1 == "paper":
        if player2 [0] == "r":
            return "player 1"
        elif player2 [0] == "s":
            return "player 2"
        else:
            return "tie"

def player_choice(player_type):
    if player_type == "c":
        player_choice = r.choice(options)
    else:
        player_choice = input("enter your choice here: ")

player1 = player_choice ("h")
player2 = player_choice("c")

test_rps(player1, player2)
