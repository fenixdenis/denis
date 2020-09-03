from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x300') # create window and size

canv = Canvas(root,bg='white') # brush window
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

def new_ball():  #create new ball
    global x,y,r
    canv.delete(ALL)

    x = 50
    y = 50
    r = 50
    canv.create_oval(x-r,y-r,x+r,y+r, fill = choice(colors), width=0)




schet = 0
def click(event):
    global schet
    print(event.x, event.y)
    print(x, y, r)
    b = event.x
    c = event.y

    #pifagor teorema for points
    ac = (x - b)**2
    bc = (y-c)**2
    se=(ac+bc)**0.5
    print(se)

    if se<=r:# count points
        schet+=1
        print(schet)

e = canv.create_oval(510, 205, 545, 240, fill='green')
b = canv.create_oval(410, 105, 445, 140, fill='black')
n = 0
dp = 11
pz =11
def dvig():
    global dp, pz
    canv.move(b, dp, pz)
    if canv.coords(b)[0] >= 800:
        dp = -dp
    if canv.coords(b)[0] <= 1:
        dp = -dp
    if canv.coords(b)[1] >= 500 or canv.coords(b)[1] <= 1:
        pz = -pz


    root.after(30,dvig)
ep =4
pq =4

def dvig1():
    global ep, pq
    canv.move(e, ep, pq)
    if canv.coords(e)[0] >= 800:
        ep = -7
    if canv.coords(e)[0] <= 1:
        ep = 7
        pq = 1
    if canv.coords(e)[1] >= 500:
        pq = -1

    root.after(30, dvig1)


def move(q,w,e,r):
    global c, pd
    b = canv.create_oval((q, w), (e, r), fill='black')
    while True:
        canv.coords(b, q+pd, w+pd, e+pd, r+pd)
        time.sleep(0.01)
        if e >=700:
            pd = -5
        if q <= 1:
            pd = 5
        print(q)
p = 1
def main():
    global p
    dvig()
    p+=1
    if p == 30:
        root.after(30,main)
dvig()
dvig1()
canv.bind('<Button-1>', click)
root.mainloop()