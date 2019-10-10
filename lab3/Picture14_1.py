import graph
import math as m


def ellipse(x0, y0, c, f):
    n = 1000
    a = []

    for num in range(n):
        x = x0 + c * m.cos(2 * m.pi * num / n)
        y = y0 + f * m.sin(2 * m.pi * num / n)
        a.append((x, y))

    result = graph.polygon(a)
    return result


graph.windowSize(450, 600)
graph.canvasSize(450, 600)

graph.brushColor("#00FFFF")
graph.rectangle(0, 0, 450, 600)

graph.brushColor("#00FF00")
graph.rectangle(0, 300, 450, 600)

graph.penColor("black")
graph.brushColor("#DEB887")
x1 = 0
y1 = 80

for i in range(15):
    graph.rectangle(x1, y1, (x1 + 30), (y1 + 250))
    x1 = x1 + 30  # 30 is wieght of zabor


def budka(x_budka, y_budka):
    graph.brushColor("#DEB887")

    x11 = x_budka
    y11 = y_budka
    graph.polygon([(x_budka, y_budka), (x_budka + 70, y_budka + 20), (x_budka + 70, y_budka + 120), (x11, y11 + 100)])

    graph.polygon([(x_budka, y_budka), (x_budka + 70, y_budka + 20),
             (x_budka + 35, y_budka - 40)])  # treangle roof

    graph.polygon([(x_budka + 35, y_budka - 40), (x_budka + 90, y_budka - 60), (x_budka + 125, y_budka),
             (x_budka + 70, y_budka + 20)])  # rectangle roof

    graph.polygon([(x_budka + 70, y_budka + 120), (x_budka + 70, y_budka + 20), (x_budka + 125, y_budka),
             (x_budka + 125, y_budka + 100)])  # right wall

    graph.brushColor("black")

    ellipse(x_budka + 35, y_budka + 60, 20, 27)  # budka enterence


def dog(x_oporn, y_oporn):

    graph.brushColor("#8B4513")
    graph.penColor("#8B4513")

    x2 = x_oporn - 70  # coordinate for head
    y2 = y_oporn - 50

    ellipse(x_oporn, y_oporn, 60, 30)  # body front

    ellipse(x_oporn - 65, y_oporn + 25, 13, 35)  # legs front upper
    ellipse(x_oporn - 10, y_oporn + 45, 13, 35)

    ellipse(x_oporn + 50, y_oporn - 15, 20, 27)  # body behing
    ellipse(x_oporn + 80, y_oporn - 15, 30, 27)
    ellipse(x_oporn + 95, y_oporn + 5, 20, 27)

    ellipse(x_oporn + 110, y_oporn + 35, 5, 25)  # legs upper behind
    ellipse(x_oporn + 60, y_oporn + 15, 5, 25)

    ellipse(x_oporn - 75, y_oporn + 60, 15, 5)  # legs under front
    ellipse(x_oporn - 21, y_oporn + 80, 15, 5)

    ellipse(x_oporn + 48, y_oporn + 39, 13, 4)  # legs under behind
    ellipse(x_oporn + 99, y_oporn + 58, 13, 4)

    graph.penColor("black")

    graph.rectangle(x2, y2, x2 + 60, y2 + 60)  # head

    ellipse(x2, y2 + 15, 10, 14)  # ears
    ellipse(x2 + 60, y2 + 15, 10, 14)

    graph.brushColor("white")  # left eye
    ellipse(x_oporn-52, y_oporn-22, 7, 3)
    graph.brushColor("black")
    ellipse(x_oporn-52, y_oporn-22, 2, 2)

    graph.brushColor("white")  # right eye
    ellipse(x_oporn-28, y_oporn-22, 7, 3)
    graph.brushColor("black")
    ellipse(x_oporn-28, y_oporn-22, 2, 2)

    x = x_oporn-60
    y = y_oporn+5

    graph.polyline(
        [(x, y), (x + 5, y - 6), (x + 8, y - 7), (x + 10, y - 8), (x + 30, y - 8), (x + 32, y - 7), (x + 35, y - 6),
         (x + 40, y)])  # mouth without tith

    graph.brushColor("white")
    graph.polygon([(x + 5, y - 6), (x + 10, y - 8), (x + 7, y - 15)])  # toth without mouth
    graph.polygon([(x + 35, y - 6), (x + 30, y - 8), (x + 33, y - 15)])


b = []


def metal_constr_left(x_budka, y_budka):
    graph.brushColor("")
    b.append(ellipse(x_budka + 20, y_budka + 85, 10, 5))  # metal near the enter
    b.append(ellipse(x_budka + 15, y_budka + 90, 5, 10))
    b.append(ellipse(x_budka + 10, y_budka + 94, 9, 4))
    b.append(ellipse(x_budka + 5, y_budka + 99, 7, 3))
    b.append(ellipse(x_budka, y_budka + 102, 8, 3))
    b.append(ellipse(x_budka - 10, y_budka + 104, 9, 3))
    b.append(ellipse(x_budka - 20, y_budka + 106, 9, 3))
    b.append(ellipse(x_budka - 22, y_budka + 114, 3, 8))
    b.append(ellipse(x_budka - 22, y_budka + 124, 3, 8))
    b.append(ellipse(x_budka - 16, y_budka + 127, 9, 3))
    b.append(ellipse(x_budka - 8, y_budka + 130, 9, 3))
    x111 = x_budka - 8
    y111 = y_budka + 130
    for num in range(6):
        b.append((ellipse(x111, y111, 9, 3)))
        x111 = x111 + 8
        y111 = y111 + 3
    return b


budka(280, 340)

dog(110, 475)


def movement():
    for num in range(0, 16):
        if num == 0:
            if graph.xCoord(a[0]) != 295:
                graph.moveObjectBy(a[0], 1, 0)
            else:
                graph.moveObjectBy(a[0], -5, 0)
        if num == 1:
            if graph.xCoord(a[1]) != 285:
                graph.moveObjectBy(a[1], -1, 0)
            else:
                graph.moveObjectBy(a[1], 5, 0)
        if num == 2:
            if graph.xCoord(a[2]) != 288:
                graph.moveObjectBy(a[2], 1, 0)
            else:
                graph.moveObjectBy(a[2], -5, 0)
        if num == 3:
            if graph.xCoord(a[3]) != 273:
                graph.moveObjectBy(a[3], -1, 0)
            else:
                graph.moveObjectBy(a[3], 5, 0)
        if num == 4:
            if graph.xCoord(a[4]) != 277:
                graph.moveObjectBy(a[4], 1, 0)
            else:
                graph.moveObjectBy(a[4], -5, 0)
        if num == 5:
            if graph.xCoord(a[5]) != 256:
                graph.moveObjectBy(a[5], -1, 0)
            else:
                graph.moveObjectBy(a[5], 5, 0)
        if num == 6:
            if graph.xCoord(a[6]) != 256:
                graph.moveObjectBy(a[6], 1, 0)
            else:
                graph.moveObjectBy(a[6], -5, 0)
        if num == 7:
            if graph.xCoord(a[7]) != 251:
                graph.moveObjectBy(a[7], -1, 0)
            else:
                graph.moveObjectBy(a[7], 4, 0)
        if num == 8:
            if graph.xCoord(a[8]) != 256:
                graph.moveObjectBy(a[8], 1, 0)
            else:
                graph.moveObjectBy(a[8], -1, 0)
        if num == 9:
            if graph.xCoord(a[9]) != 250:
                graph.moveObjectBy(a[9], -1, 0)
            else:
                graph.moveObjectBy(a[9], 5, 0)
        if num == 10:
            if graph.xCoord(a[10]) != 270:
                graph.moveObjectBy(a[10], 1, 0)
            else:
                graph.moveObjectBy(a[10], -5, 0)
        if num == 12:
            if graph.xCoord(a[12]) < 285:
                graph.moveObjectBy(a[12], 1, 0)
            else:
                graph.moveObjectBy(a[12], -5, 0)
        if num == 13:
            if graph.xCoord(a[13]) < 290:
                graph.moveObjectBy(a[13], 1, 0)
            else:
                graph.moveObjectBy(a[13], -5, 0)
        if num == 14:
            if graph.xCoord(a[14]) < 295:
                graph.moveObjectBy(a[14], 1, 0)
            else:
                graph.moveObjectBy(a[14], -5, 0)
        if num == 15:
            if graph.xCoord(a[15]) < 300:
                graph.moveObjectBy(a[15], 1, 0)
            else:
                graph.moveObjectBy(a[15], -5, 0)


graph.onTimer(movement, 100)

a = metal_constr_left(280, 340)

graph.run()
