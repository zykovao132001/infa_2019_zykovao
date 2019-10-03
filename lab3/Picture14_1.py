from graph import *

windowSize(450, 600)
canvasSize(450, 600)

brushColor("#00FFFF")
rectangle(0, 0, 450, 600)

brushColor("#00FF00")
rectangle(0, 300, 450, 600)

penColor("black")
brushColor("#DEB887")
x1 = 0
y1 = 80

for i in range(15):
    rectangle(x1, y1, (x1 + 30), (y1 + 250))
    x1 = x1 + 30  # 30 is wieght of zabor


def budka(x_budka, y_budka):
    brushColor("#DEB887")

    x11 = x_budka
    y11 = y_budka
    polygon([(x_budka, y_budka), (x_budka + 70, y_budka + 20), (x_budka + 70, y_budka + 120), (x11, y11 + 100)])

    polygon([(x_budka, y_budka), (x_budka + 70, y_budka + 20),
             (x_budka + 35, y_budka - 40)])  # treangle roof

    polygon([(x_budka + 35, y_budka - 40), (x_budka + 90, y_budka - 60), (x_budka + 125, y_budka),
             (x_budka + 70, y_budka + 20)])  # rectangle roof

    polygon([(x_budka + 70, y_budka + 120), (x_budka + 70, y_budka + 20), (x_budka + 125, y_budka),
             (x_budka + 125, y_budka + 100)])  # right wall

    brushColor("black")

    circle(x_budka + 35, y_budka + 60, 20, 27)  # budka enterence


def dog(x_oporn, y_oporn):

    brushColor("#8B4513")
    penColor("#8B4513")

    x2 = x_oporn - 70  # coordinate for head
    y2 = y_oporn - 50

    circle(x_oporn, y_oporn, 60, 30)  # body front

    circle(x_oporn - 65, y_oporn + 25, 13, 35)  # legs front upper
    circle(x_oporn - 10, y_oporn + 45, 13, 35)

    circle(x_oporn + 50, y_oporn - 15, 20, 27)  # body behing
    circle(x_oporn + 80, y_oporn - 15, 30, 27)
    circle(x_oporn + 95, y_oporn + 5, 20, 27)

    circle(x_oporn + 110, y_oporn + 35, 5, 25)  # legs upper behind
    circle(x_oporn + 60, y_oporn + 15, 5, 25)

    circle(x_oporn - 75, y_oporn + 60, 15, 5)  # legs under front
    circle(x_oporn - 21, y_oporn + 80, 15, 5)

    circle(x_oporn + 48, y_oporn + 39, 13, 4)  # legs under behind
    circle(x_oporn + 99, y_oporn + 58, 13, 4)

    penColor("black")

    rectangle(x2, y2, x2 + 60, y2 + 60)  # head

    circle(x2, y2 + 15, 10, 14)  # ears
    circle(x2 + 60, y2 + 15, 10, 14)

    brushColor("white")  # left eye
    circle(x_oporn-52, y_oporn-22, 7, 3)
    brushColor("black")
    circle(x_oporn-52, y_oporn-22, 2, 2)

    brushColor("white")  # right eye
    circle(x_oporn-28, y_oporn-22, 7, 3)
    brushColor("black")
    circle(x_oporn-28, y_oporn-22, 2, 2)

    x = x_oporn-60
    y = y_oporn+5

    polyline(
        [(x, y), (x + 5, y - 6), (x + 8, y - 7), (x + 10, y - 8), (x + 30, y - 8), (x + 32, y - 7), (x + 35, y - 6),
         (x + 40, y)])  # mouth without tith

    brushColor("white")
    polygon([(x + 5, y - 6), (x + 10, y - 8), (x + 7, y - 15)])  # toth without mouth
    polygon([(x + 35, y - 6), (x + 30, y - 8), (x + 33, y - 15)])


def metal_constr(x_budka, y_budka):
    brushColor("")
    circle(x_budka + 20, y_budka + 85, 10, 5)  # metal near the enter
    circle(x_budka + 15, y_budka + 90, 5, 10)
    circle(x_budka + 12, y_budka + 94, 9, 4)
    circle(x_budka + 5, y_budka + 99, 7, 3)
    circle(x_budka, y_budka + 102, 8, 3)
    circle(x_budka - 10, y_budka + 104, 9, 3)
    circle(x_budka - 20, y_budka + 106, 9, 3)
    circle(x_budka - 22, y_budka + 114, 3, 8)
    circle(x_budka - 22, y_budka + 124, 3, 8)
    circle(x_budka - 16, y_budka + 127, 9, 3)
    circle(x_budka - 8, y_budka + 130, 9, 3)
    x111 = x_budka - 8
    y111 = y_budka + 130
    for num in range(6):
        circle(x111, y111, 9, 3)
        x111 = x111 + 8
        y111 = y111 + 3


budka(280, 340)

dog(110, 475)

metal_constr(280, 340)

run()
