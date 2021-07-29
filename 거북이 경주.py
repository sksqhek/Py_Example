import turtle as t
import random

t1 = t.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.penup()
t1.goto(-500, 0)
t1.pendown()
t1.speed(1)

t2 = t.Turtle()
t2.shape("turtle")
t2.color("pink")
t2.penup()
t2.goto(-500, 100)
t2.pendown()
t2.speed(1)

t.speed(0)
t.penup()
t.goto(500, -50)
t.pendown()
t.goto(500, 150)
t.penup()
t.goto(-100, -150)

def turtle_move(x):
    rnd = random.randint(0,10)
    x.goto(x.position()[0] + rnd, x.position()[1])

while True:
    turtle_move(t1)
    turtle_move(t2)

    if t1.position()[0] >= 500 and t2.position()[0] < 500:
        t.write("파랑 거북이가 이겼습니다.", font=('', 20, "bold"))
        break
    elif t1.position()[0] < 500 and t2.position()[0] >= 500:
        t.write("분홍 거북이가 이겼습니다.", font=('', 20, "bold"))
        break
    elif t1.position()[0] >= 500 and t2.position()[0] >= 500:
        t.write("두 거북이가 비겼습니다.", font=('', 20, "bold"))
        break

t.done()