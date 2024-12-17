#Gracie oxnam
#mastermind game

import random as r

digits = ["1","2","3","4","5","6","7","8","9","0"]
r.shuffle(digits)
code = digits[:4]
#attempt = 

print(code)

print("Try to guess my seceret code\nI will give you hints to get closer")
guess = [input("enter your guess here: ")]
            
while (guess) != (code): #or attempt >10:
    for n in range (0,4):
        if guess[0] == code[0]:
      print("green")
    elif guess[0] == code[0:]:
        print("yellow")
    else: print("red")
    guess = input("guess again")
    if guess[in
print("yay")

for i in range (len(guess)-1):
    for j in range (i+1,len(guess)):
        if guess[i] == guess[j]:
            print("green")
