import tkinter as tk
from random import randrange as rnd, c
import time
import math

root = tk.Tk()

root.geometry('800x600')

canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red', 'orange','yellow', 'green','blue']

Balls = []

g = 10
dt = 10
n = 10

tim = 0


class Shape:
    def __init__(self, color):
        self.color = color
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dx = rnd(-10, 10)
        self.dy = rnd(-10, 10)
        self.obj = 0

    def draw(self):
        for i in Balls:
            if ((self.x - i.x) ** 2) + ((self.y - i.y) ** 2)  >= ((self.r + i.r) ** 2):
                self.obj = canv.create_oval(self.x - self.r, self.y - self.r,
                                            self.x + self.r, self.y + self.r,
                                            fill=self.color, width=0)

    def move(self):
        for i in ball:
            if ((self.x - i.x) ** 2) + ((self.y - i.y) ** 2) <= ((self.r + i.r) ** 2):
                self.dx = - sefl.dx
                self.dy = - sefl.dy
        if (self.x - self.r) <= 0:
            self.dx = - self.dx
        if (self.x + self.r) >= 800:
            self.dx = - self.dx
        if (self.y - self.r) <= 0:
            self.dy = - self.dy
        if (self.y + self.r) >= 600:
            self.dy = - self.dy

        self.x += self.dx
        self.y += self.dy

    def axelaration(self):
        global tim
        global g
        self.dx = self.dx + (g * math.cos(tim))
        self.dy = self.dy + (g * math.sin(tim))
        if tim >= (2 * math.pi):
            tim = tim - 2 * math.pi
        else:
            tim = tim + 0.1

    def show(self):
        canvas.move(self.obj, self.dx, self.dy)

def tick():
    global dt

    for i in balls:
        ball.move()
        ball.show()
    root.after(dt, tick)


class Game:
    def __init__(self):
        self.score = 0

    def canvas_click_handler(self, event):
        for i in balls:
            if ((i.x - event.x) ** 2) + ((i.y - event.y) ** 2) <= i.r:
                self.score += 1
        print(str(self.score))

    def main(self):
        global root, canvas,







tk.mainloop()