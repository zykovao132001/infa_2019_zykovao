from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
POINTS = 0
BULLET = 0

# class Treangles:
#     def __init__(self, x1, y1, x2, y2, x3, y3, vx, vy):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
#         self.vx = vx
#         self.vy = vy
#         self.color = 'blue'
#         self.id = canv.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill=self.color)
#
#     def move(self):
#         self.x1 += self.vx
#         self.x2 += self.vx
#         self.x3 += self.vx
#         self.y1 += self.vy
#         self.y2 += self.vy
#         self.y3 += self.vy
#         canv.move(self.id, self.vx, self.vy)
#
#     def wall_normal_movement(self):
#         if ((self.x1 or self.x2 or self.x3) < 0) or ((self.x1 or self.x2 or self.x3) > 800):
#             self.vx *= -1
#         if (self.y1 or self.y2 or self.y3) < 0:
#             self.vy *= -1
#         if (self.y1 or self.y2 or self.y3) > 600:
#             self.vy = 0
#             self.vx = 0


class ball:

    def __init__(self, n=0, x=40, y=450, vx=0, vy=0):
        self.points_basic = []
        self.x = x
        self.y = y
        self.r = 10
        self.n = n
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        if n == 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        else:
            for i in range(self.n):
                self.points_basic.append(
                    (self.x + (self.r * math.sin((2 * i + 0.5 * n) * math.pi/ self.n)),
                     self.y + (self.r * math.cos((2 * i + 0.5 * n) * math.pi / self.n))))
            self.id = canv.create_polygon(self.points_basic, fill=self.color)
        self.live = 7

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def walltest(self):
        if self.x - self.r < 0 or self.x + self.r > 800:
            self.vx *= -1
        elif self.y - self.r < 0 or self.y + self.r > 600:
            self.vy *= -1

    def move(self):
        self.live -= 0.03
        self.x += self.vx
        self.y += self.vy + 0.1
        self.vy += 0.1
        canv.move(self.id, self.vx, self.vy)
        self.walltest()

    def hittest(self, obj):
        if obj.n != 4 and math.hypot((self.x - obj.x), (self.y - obj.y)) <= math.hypot((self.r + obj.r), 0):
            return True
        elif obj.n == 4 and abs(self.x - obj.x) <= self.r + obj.r and abs(self.y - obj.y) <= self.r + obj.r:
            return True
        else:
            return False

    def __del__(self):
        if self.n != 0:
            canv.delete(self.id)
        else:
            canv.delete(self.id)
            # for i in range(self.n):
            #     canv.create_polygon(self.x, self.y, self.x +



# class Treangle:
#     def __init__(self, x1, y1, x2, y2, x3, y3, vx, vy):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
#         self.vx = vx
#         self.vy = vy
#         self.color = choice(['blue', 'green', 'red', 'brown'])
#         self.id = canv.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill=self.color)
#         self.live = 5
#
#     def walltest(self):
#         if (self.x1 or self.x2 or self.x3 < 0) or (self.x1 or self.x2 or self.x3) > 800:
#             self.vx *= -1
#         elif (self.y1 or self.y2 or self.y3 < 0) or (self.y1 or self.y2 or self.y3) > 800:
#             self.vy *= -1
#
#     def move(self):
#         self.live -= 0.03
#         self.x1 += self.vx
#         self.x2 += self.vx
#         self.x3 += self.vx
#         self.y1 += self.vy
#         self.y2 += self.vy
#         self.y3 += self.vy
#         self.vy += 0.1
#         canv.move(self.id, self.vx, self.vy)
#         self.walltest()
#         if self.live < 0:
#           canv.delete(self.id)

class Gun:

    def __init__(self, x=20, y=450, vx=0, vy=0, v=5):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.v = v
        self.f2_power = 1
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)
        self.rot = False

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet, BULLET
        bullet += 1
        BULLET += 1
        new_ball = ball(n=choice([0, 4, 5]), x=self.x + max(self.f2_power * 5, 20) * math.cos(self.an),
                    y=self.y + max(self.f2_power * 5, 20) * math.sin(self.an))
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) + self.vx
        new_ball.vy = self.f2_power * math.sin(self.an) + self.vy
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 1

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - self.y) / (event.x - self.x)) + math.pi * (math.copysign(1, event.x - self.x) - 1) / 2
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power * 5, 20) * math.cos(self.an),
                    self.y + max(self.f2_power * 5, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 20:
                self.f2_power += 0.2
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def walltest(self):
        if not self.rot:
            if self.x < 5 or self.x > 795:
                self.vx *= -1
                self.rot = True
            if self.y < 5 or self.y > 595:
                self.vy *= -1
                self.rot = True
        elif 5 < self.x < 795 and 5 < self.y < 595:
            self.rot = False

    def move(self, event=0):
        self.walltest()
        if not self.rot:
            self.vy = self.v * math.sin(self.an)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)


class Target:

    def __init__(self, n=0):
        self.x = rnd(520, 760)
        self.points_basic = []
        self.y = rnd(120, 530)
        self.Ax = self.x - 620
        self.Ay = self.y - 325
        self.n = n
        self.time = time.time()
        self.r = rnd(5, 20)
        self.color = 'red'
        self.points = 0
        self.live = 1
        if self.n == 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        else:
            for i in range(self.n):
                self.points_basic.append(
                    (self.x + (self.r * math.sin(2 * i * math.pi / self.n)),
                     self.y + (self.r * math.cos(2 * i * math.pi / self.n))))
            self.id = canv.create_polygon(self.points_basic, fill=self.color)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        global POINTS
        canv.coords(self.id, -10, -10, -10, -10)
        POINTS += points

    def move(self):
        canv.move(self.id,
                  self.Ax * math.cos(time.time() - self.time) + 620 - self.x + 20 * math.sin(
                      5 * (time.time() - self.time)),
                  self.Ay * math.cos(time.time() - self.time) + 325 - self.y + 20 * math.sin(
                      5 * (time.time() - self.time)))
        self.x = self.Ax * math.cos(time.time() - self.time) + 620 + 20 * math.sin(5 * (time.time() - self.time))
        self.y = self.Ay * math.cos(time.time() - self.time) + 325 + 20 * math.sin(5 * (time.time() - self.time))



screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []
screen2 = canv.create_text(30, 30, text=str(POINTS) + ' : ' + str(BULLET), font='28')


def new_game():
    global gun, screen1, balls, bullet, POINTS, BULLET
    t1 = Target()
    t2 = Target(4)
    t3 = Target(5)
    bullet = 0
    balls = []
    treangles = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    t3.live = 1
    while t1.live or balls or t2.live or t3.live:
        i = 0
        while i < len(balls):
            balls[i].move()
            if (balls[i].hittest(t1) or balls[i].hittest(t2) or balls[i].hittest(t3)) and (t1.live or t2.live or t3.live):
                t1.live = 0
                t2.live = 0
                t3.live = 0
                t1.hit()
                t2.hit()
                t3.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canv.itemconfig(screen2, text=str(POINTS) + ' : ' + str(BULLET))
            if balls[i].live < 0:
                balls.pop(i)


            i += 1
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
        g1.move()
        t1.move()
        t2.move()
        t3.move()
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(3, new_game)


new_game()
root.mainloop()