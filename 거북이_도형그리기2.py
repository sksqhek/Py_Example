import turtle, random

t = turtle.Turtle()
turtle.setup(1000, 1000, 0, 0)
t.speed(0)
count = 1


def rect(n):
    for a in range(n):
        t.fd(100)
        t.rt(360 / n)


def f(n):
    for b in range(10):
        global count
        r = random.random()
        g = random.random()
        b = random.random()
        size = random.randint(1, 10)
        dis = random.randint(1, 100)
        xpos = random.randint(-200, 200)
        ypos = random.randint(-200, 200)
        t.penup()
        t.goto(xpos, ypos)
        t.pendown()
        t.pensize(size)
        t.color(r, g, b)
        if count % 2 == 0:
            rect(n)
            count = +1
        else:
            t.begin_fill()
            rect(n)
            t.end_fill()
            count += 1

shapes = [4,3,5,6,8]

for s in shapes:
    f(s)
