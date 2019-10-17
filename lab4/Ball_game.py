import tkinter as tk
from random import randrange as rnd, choice
import time
"""
-установил 3й питон 
-напиал класс меню

"""

root = tk.Tk()
# geomerty(width x height)
root.geometry('800x600')

canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red','orange','yellow', 'green','blue']

class Shape:
    def __init__(self, color):
        self.color = color
        self.x0 = rnd(100, 700)
        self.y0 = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dx = rnd(-10, 10)
        self.dy = rnd(-10, 10)
        self.obj = None

    def draw(self):
        self.obj = canv.create_oval(self.x0 - self.r, self.y0 - self.r,
                                           self.x0 + self.r, self.y0 + self.r,
                                           fill=self.color, width=0)
        self.move()

    def move(self):
        if canv.coords(self.obj)[2] >= 800 or canv.coords(self.obj)[0] <= 0:
            self.dx = - self.dx
        if canv.coords(self.obj)[3] >= 600 or canv.coords(self.obj)[1] <= 0:
            self.dy = - self.dy

        canv.move(self.obj, self.dx, self.dy)
        root.after(10, self.move)
        print(self.x, self.y)



ball1 = Shape(choice(colors))
ball1.draw()
ball2 = Shape(choice(colors))
ball2.draw()
ball3 = Shape(choice(colors))
ball3.draw()

def main_timer():
    global ball1, ball2, ball3
    root.after(10, ball1.move)
    root.after(10, ball2.move)
    root.after(10, ball3.move)

#def click(event):
#    print('click')

#canv.bind('<Button-1>', click)
tk.mainloop()