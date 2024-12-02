#gracie oxnam
#turtle artwork

import turtle
import random as r

#import two turtles
tom = turtle.Turtle()
terry = turtle.Turtle()

colors = ['pink','hot pink','purple','yellow','blue','light blue','red',
          'orange']

#create function where turtle has 1 parameter, 1 loop, use random, 1 if statement
def rhombus():
    for i in range(2):
        terry.forward(100)
        terry.left(45)
        terry.forward(100)
        terry.left(135)

def draw():
    terry.pencolor(colors[r.randint(0,8)])
    for i in range(8):
        rhombus()
        terry.left(20)
    tom.pensize(r.randint(1,20))
    if tom.pensize() > 10:
        tom.pencolor('green')
    tom.right(90)
    tom.forward(200)

double = tom.right(45) + terry.right(45)
        

#call function twice with different values
draw()
draw(double)

