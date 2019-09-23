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
    x1 = x1 + 30

polygon([(280,340), (350,360), (350,460), (280,440 )])

polygon([(280, 340), (350,360), (315, 300)])

polygon([(315, 300), (370, 280), (405, 340), (350,360)])

polygon([(350,460), (350,360), (405, 340), (405, 440)])

brushColor("black")

circle(315, 400, 20, 27)

brushColor("#8B4513")
penColor("#8B4513")

x2 = 40
y2 = 425

circle(110, 475, 60, 30) #переднее тело

circle(45, 500, 13, 35) #ноги передние верхние
circle(100, 520, 13, 35)



circle(160, 460, 20, 27) #тело заднее
circle(190, 460, 30, 27)
circle(205, 480, 20, 27)

circle(220, 510, 5, 25) #ноги задние верхние
circle(170, 490, 5, 25)

circle(35, 535, 15, 5) #ноги передние нижние
circle(89, 555, 15, 5)

circle(158, 514, 13, 4) #ноги задние нижние
circle(209, 533, 13 ,4)


penColor("black")
rectangle(x2, y2, x2 + 60, y2 + 60) #голова основа

circle(40, 440, 10, 14) #уши на голове
circle(100, 440, 10 ,14)


brushColor("white") #глаз левый
circle(58, 453, 7, 3)
brushColor("black")
circle(58, 453, 2, 2)


brushColor("white")  #глаз правый
circle(82, 453, 7, 3)
brushColor("black")
circle(82, 453, 2, 2)

x = 50
y = 480

polyline([(x, y), (x+5, y-6), (x+8, y-7), (x+10, y-8), (x+30, y-8), (x+32, y-7), (x+35, y-6), (x+40, y)]) #рот без зубов

brushColor("white")
polygon([(x+5, y-6), (x+10, y-8), (x+7, y-15)])    #зубы без рта
polygon([(x+35, y-6), (x+30, y-8), (x+33, y-15)])


brushColor("")
circle(300, 425, 10, 5) #цепь начало от входа
circle(295, 430, 5, 10)
circle(292, 434, 9, 4)
circle(285, 439, 7, 3)
circle(280, 442, 8, 3)
circle(270, 444, 9, 3)
circle(260, 446, 9, 3)
circle(258, 454, 3, 8)
circle(258, 464, 3, 8)
circle(264, 467, 9, 3)
circle(272, 470, 9, 3)
x11 = 272
y11 = 470
for i in range(6):
    circle(x11, y11, 9, 3)
    x11 = x11 + 8
    y11 = y11 + 3






run()
