import tkinter as tk
from random import randrange as rnd, choice
import time

root = tk.Tk()
root.geometry('800x600')

canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red','orange','yellow', 'green','blue']


class Object:
    def __init__(self, shape):
        self.shape = shape
        self.color = choice(colors)
        self.size = rnd(30, 50)
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)

    def create_ball(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        if self.shape == "circle":

            canv.delete(tk.ALL)
            self.shape = "circle"
            self.x = rnd(100, 700)
            y = rnd(100, 500)
            size = rnd(30, 50)
            color = choice(colors)
            canv.create_oval(self.x - size, y - size, self.x + size, y + size, fill= color, width=0)
            root.after(1000, self.create_ball)


ob = Object("circle")
ob.create_ball()


def click(event):
    print('click')

canv.bind('<Button-1>', click)





root.mainloop()