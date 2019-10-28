import tkinter as tk
from random import randrange as rnd
import random
import math

colors = ['red', 'orange', 'yellow', 'green', 'blue']

g = 0.1
dt = 1
n = 5

tim = 0

H = 800
W = 600


class Shape:
    def __init__(self):
        global H, W
        self.col = colors[random.randint(0, 4)]
        self.x = rnd(100, W - 100)
        self.y = rnd(100, H - 100)
        self.r = rnd(30, 50)
        self.dx = (rnd(-1, 1) * 1)
        self.dy = (rnd(-1, 1) * 1)

        for ball in balls:
            while (ball.r + self.r) ** 2 >= (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2:
                self.x = rnd(100, W - 100)
                self.y = rnd(100, H - 100)
        self.obj = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.col)

    def move(self):

        self.x += self.dx
        self.y += self.dy

        global tim
        global g
        self.dx = self.dx + (g * math.cos(tim))
        self.dy = self.dy + (g * math.sin(tim))
        if tim >= (2 * math.pi):
            tim = tim - 2 * math.pi
        else:
            tim = tim + 0.01

        for ball in balls:
            if (self != ball) and (((self.x - ball.x) ** 2) + ((self.y - ball.y) ** 2) <= ((self.r + ball.r) ** 2)):
                self.dx = - self.dx
                self.dy = - self.dy

        if (self.x - self.r) <= 0:
            self.dx = - self.dx
            self.x = self.r
        if (self.x + self.r) >= W:
            self.dx = - self.dx
            self.x = W - self.r
        if (self.y - self.r) <= 0:
            self.dy = - self.dy
            self.y = self.r
        if (self.y + self.r) >= H:
            self.dy = - self.dy
            self.y = H - self.r

        self.dx *= 0.995
        self.dy *= 0.995

    def show(self):
        canvas.delete(self.obj)
        self.obj = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.col)


def tick():
    global dt
    for ball in balls:
        ball.move()
        ball.show()
    root.after(dt, tick)


class Game:
    def __init__(self):
        self.score = 0

    def click_score(self, event):
        for ball in balls:
            if ((ball.x - event.x) ** 2) + ((ball.y - event.y) ** 2) <= ball.r ** 2:
                self.score += 1
        print(str(self.score))

    def main(self):
        global root, canvas, balls
        global g, dt, n

        root = tk.Tk()
        root.geometry(str(W) + "x" + str(H))
        canvas = tk.Canvas(root, bg='white')
        canvas.pack(fill=tk.BOTH, expand=1)
        canvas.bind('<Button-1>', self.click_score)
        balls = []
        for i in range(n):
            balls.append(Shape())

        tick()
        root.mainloop()


start = Game()
start.main()
tk.mainloop()