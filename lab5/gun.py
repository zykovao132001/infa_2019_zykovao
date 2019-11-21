from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, n: int=0, x=40, y=450, points=[], vx=0, vy=0):
        self.x = x # start position
        self.y = y # start position
        self.r = rnd(10, 30)
        self.vx = vx # start velocity
        self.vy = vy # start velocity
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.n = max(n, len(points))
        self.live = 40
        if self.n == 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        else:
            if not points:
                for i in range(self.n):
                    points.append(
                        (self.x + (self.r * math.sin(2 * i * math.pi / self.n)),
                        self.y + (self.r * math.cos(2 * i * math.pi / self.n))))
            self.id = canv.create_polygon(points, fill=self.color)
        self.points = points

    # def set_coords(self):
    #     canv.coords(
    #         self.id,
    #         self.x - self.r,
    #         self.y - self.r,
    #         self.x + self.r,
    #         self.y + self.r
    #     )

    def move(self):
        if ((self.x + self.vx + self.r) > 800) or ((self.x + self.vx - self.r) < 0):
            self.vx *= -1
        if ((self.y + self.vy + self.r) > 600) or ((self.y + self.vy - self.r) < 0):
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        self.vy += 0
        self.vx += 0
        self.live -= 0.2
        canv.move(self.id, self.vx, self.vy)

    def hittest(self, obj):
        if obj.n != 4 and math.hypot((self.x - obj.x), (self.y - obj.y)) <= math.hypot((self.r + obj.r), 0):
            return True
        elif obj.n == 4 and abs(self.x - obj.x) <= self.r + obj.r and abs(self.y - obj.y) <= self.r + obj.r:
            return True
        else:
            return False

    def __del__(self):
        canv.delete(self.id)


class Gun:
    def __init__(self, x=20, y=450):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = x
        self.y = y
        self.vx = 1
        self.vy = 3
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

    def move(self):
        if ((self.x + 30 + self.vx) > 50) or ((self.x - 30 + self.vx) < 0):
            self.vx = - self.vx
            if (self.x + 30 + self.vx) > 50:
                self.x = 50 - 30 - self.vx
            if (self.x - 30 + self.vx) < 0:
                self.x = 0 - self.vx + 30

        if ((self.y - 30 + self.vy) > 500) or ((self.y + 30 + self.vy) < 50):
            self.vy = - 0.7 * self.vy
            if (self.y - 30 + self.vy) > 500:
                self.y = 500 + 30 - self.vy
            if (self.y + 30 + self.vy) < 50:
                self.y = 50 - self.vy - 30
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )
        #canv.move(self.id, self.vx, self.vy)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(choice([0, 4, 5]), self.x, self.y)
        print(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = + self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-self.y) / (event.x-self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self, n: int = 0, points=[]):
        self.game_points = 0
        target_points = []
        self.n = max(n, len(points))
        self.points = points
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.live = 1
        self.vx = rnd(-5, 5)
        self.vy = rnd(-10, 10)
        self.x = rnd(150, 450)
        self.y = rnd(150, 450)
        self.r = rnd(5, 20)
        self.color = 'red'
        if self.n == 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        else:
            if not points:
                for n in range(self.n):
                    points.append(
                        (self.x + (self.r * math.sin(2 * n * math.pi / self.n)),
                        self.y + (self.r * math.cos(2 * n * math.pi / self.n))))
            self.id = canv.create_polygon(points, fill=self.color)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.itemconfig(self.id, fill=color)

    def hit(self, game_points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.game_points += game_points
        canv.itemconfig(self.id_points, text=self.game_points)



    def move(self):
        if ((self.x + self.r + self.vx) > 800) or ((self.x - self.r + self.vx) < 0):
            self.vx = - 0.9 * self.vx
        if ((self.y + self.r + self.vy) > 600) or ((self.y - self.r + self.vy) < 100):
            self.vy = - 0.7 * self.vy
        self.x += self.vx
        self.y += self.vy
        self.vy += 1
        canv.move(self.id, self.vx, self.vy)


t1 = Target(4)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global g1, t1, screen1, balls, bullet
    t1.new_target()
    t1.move()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    t1.live = 1
    while t1.live or balls:
        i = 0
        while i < len(balls):
            balls[i].move()
            # balls[i].set_coords()
            if balls[i].hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
            if balls[i].live < 0:
                # for n in range(balls[i].n):
                #     balls.append(ball(points=[(balls[i].points[n], balls[i].points[(n + 1) % (balls[i].n)]),
                #                               (balls[i].x, balls[i].y)], vx=balls[i].vx + math.sin(2 * math.pi / balls[i].n),
                #                             vy=balls[i].vy + math.cos(2 * math.pi / balls[i].n)))
                balls.pop(i)
            else:
                i += 1
        canv.update()
        time.sleep(0.03)
        g1.move()
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(g1)
    root.after(5, new_game)


new_game()
root.mainloop()
