from graph import *
def update():
    moveObjectBy(ship, 5,0)


def circl(x, y, r, z):
    penColor('black')
    penSize(1)
    brushColor(z)
    circle(x,y,r)

def pr(x, y, x2, y2,z):
    penColor('black')
    penSize(0)
    brushColor(z)
    rectangle(x, y, x2, y2)

canvasSize(800, 800)
windowSize(800, 800)

#sky,water,erth
pr(0,0,800,300,'cyan')
pr(0,300,800,500,'blue')
pr(0,500,800,800,'yellow')

circl(700, 70, 55,'yellow')# sun
sun = circle(700,70,55)
#oblaka
def oblaka():
    x = 150
    y = 70
    b = 0
    for i in range(3):
        circl(x + 30, y - 30, 30, 'white')
        circl(x,y,30, 'white')
        x+=40
        b+=1
        if b == 3:
            circl(x, y, 30, 'white')
dx = 5

def update():
    global dx
    if xCoord(ship) >= 379:
        dx = -7
    if xCoord(ship) <= 1:
        dx = 7
        print(1)
    moveObjectBy(ship, dx, 0)
oblak = oblaka()

pd = 5
def update1():
    global pd
    if xCoord(sun) >= 379:
        pd = -7
    if xCoord(sun) <= 1:
        pd = 7
        print(1)
    moveObjectBy(sun, pd, 0)

#ship
ship = rectangle(400,320,700,380)


p = [[700, 319], [785,320], [700,380]]
penColor('black')
brushColor('brown')
polygon(p)

onTimer(update1,50)
onTimer(update,50)








run()