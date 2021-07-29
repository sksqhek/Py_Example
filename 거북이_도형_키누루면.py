import turtle

t = turtle.Turtle()

draw_action = 4
draw_color = 1

def new_clear():
    global draw_action
    t.clear()
    t.pensize(1)
    t.pendown()
    draw_action = 1


def square_draw(length):
    for i in range(4):
        t.forward(length)
        t.left(360 / 4)

def triangle_draw(length):
    for i in range(3):
        t.forward(length)
        t.left(360 / 3)

def pentagon_draw(length):
    for i in range(5):
        t.forward(length)
        t.left(360 / 5)

def drawit(x, y):
    global draw_action

    if draw_color == 1:
        t.color("blue")
    elif draw_color == 2:
        t.color("red")
    elif draw_color == 3:
        t.color("green")

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    if draw_action == 4:
        triangle_draw(50)
    elif draw_action == 5:
        square_draw(50)
    elif draw_action == 6:
        pentagon_draw(50)

    t.end_fill()

s = turtle.Screen()
s.onscreenclick(drawit)


def blue():
    global draw_color
    draw_color = 1


def red():
    global draw_color
    draw_color = 2


def green():
    global draw_color
    draw_color = 3


def triangle():
    global draw_action
    draw_action = 4


def sqauare():
    global draw_action
    draw_action = 5


def pentagon():
    global draw_action
    draw_action = 6


s.onkey(blue, 'b')
s.onkey(red, 'r')
s.onkey(green, "g")
s.onkey(triangle, "3")
s.onkey(sqauare, "4")
s.onkey(pentagon, "5")
s.listen()#추가

turtle.mainloop()