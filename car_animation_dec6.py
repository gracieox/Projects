#gracie oxnam
#DrawingPanel practice
#create a car driving

import DrawingPanel

drive = DrawingPanel.DrawingPanel (800,600)
def background():
    drive.fill_rect(0,0,800,600,'white')
    drive.fill_rect(0,426,800,400,'dark green')
    drive.fill_oval(600,50, 100,100,'orange')
    drive.fill_oval(30,80,60,60,'light blue')
    drive.fill_oval(50,50,80,80,'light blue')
    drive.fill_oval(70,80,70,70,'light blue')

def car (x,y):
    drive.fill_rect(x,y, 50,15,'red')
    drive.fill_rect(x+10,y-10, 30,20,'red')
    drive.fill_oval(x+7,y+10, 15,15,'black')
    drive.fill_oval(x+28,y+10, 15,15,'black')

def kid ():
    drive.fill_rect(550,400,10,25,'brown')
    #drive.fill_polygon(
    drive.fill_oval(550,390,10,10,'brown')
    
x = 0
for i in range (50):
    drive.sleep(1000/60)  
    y = 400
    x = x+10
    background()
    kid()
    car(x,y)
    
