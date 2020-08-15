from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=999, height=999)

canvas.pack()

canvas.create_polygon(10,300,10,90,50,35)
for i in range(0,600):
    canvas.move(1,5,5)
    tk.update()
    time.sleep(0.05)


mainloop()