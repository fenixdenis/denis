from graph import *

def circl(x, y, r, z):
    penColor('black')
    penSize(1)
    brushColor(z)
    circle(x,y,r)

def pr(x, y, x2, y2):
    penColor('black')
    penSize(1)
    brushColor('black')
    rectangle(x, y, x2, y2)

def stro(x, y, x1, y1):
    penColor('black')
    penSize(1)

    for i in range(50):
        line(x, y, x1, y1)
        y-=0.5
        y1-=0.5
        x+=0.5
        x1+=0.5

def lom(p):
    a = 0
    b = len(p)
    for i in range(300):
        polyline(p)
        for j in range(b):

            p[j][a + 1] += 0.5

canvasSize(1000, 1000)
windowSize(1000, 1000)
penColor('black')
penSize(1000)
p = ([20,40], [30, 50], [50,30],[200,40], [300, 50], [500,30])
lom(p)





run()