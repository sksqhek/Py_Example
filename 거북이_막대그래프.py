import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def bar(x, y, value, color = "blue"):
    t.begin_fill()
    t.color(color)
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.goto(x + 10, 0)
    t.goto(x + 10, value*10)
    t.goto(x, value*10)
    t.goto(x, 0)
    t.end_fill()

    t.goto(x + 10, value * 10)
    t.write(value)

if __name__ == '__main__':
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(180, 0)
    t.goto(175, 5)
    t.goto(180, 0)
    t.goto(175, -5)

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(0, 180)
    t.goto(5, 175)
    t.goto(0, 180)
    t.goto(-5, 175)

    while True:
        x = int(input("x좌표 입력(y=0, x=-1 to quirt!)"))
        if x == -1:
            break
        value = int(input("값 입력(0 ~ 19): "))
        bar(x,0,value)

    turtle.mainloop()