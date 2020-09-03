from graph import *

def update():
    moveObjectBy(obj,5,0)
    if xCoord(obj)<=380:
        close()

brushColor('blue')
rectangle(0,0,400,400)
x = 100
y = 100

penColor('yellow')
brushColor('yellow')

obj = rectangle(x,y,x+20,y+20)

def qwe():
    if xCoord(obj) > 0:
        moveObjectBy(obj, -5, 0)

def update():
    global dx
    if xCoord(obj) >= 379:
        dx = -7
    if xCoord(obj) <= 1:
        dx = 7
        print(1)
    moveObjectBy(obj, dx, 0)

onTimer(update,50)

run()