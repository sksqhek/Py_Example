import turtle

import random

s = turtle.Screen()
image1 = "1.gif"
image2 = "2.gif"

s.addshape(image1)
s.addshape(image2)


t1 = turtle.Pen()
t1.shape(image1)
t1.pensize(5)
t1.penup()
t1.goto(-300, 0)


t2 = turtle.Pen()
t2.shape(image2)
t2.pensize(5)
t2.penup()
t2.goto(-300, -200)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

result = turtle.Pen()
result.penup()
result.goto(300, -80)


while t1.pos()[0] < 300 and t2.pos()[0] < 300:
    d1 = random.randint(1, 60)
    d2 = random.randint(1, 60)
    t1.forward(d1)
    t2.forward(d2)

if t1.pos()[0] > t2.pos()[0]:
    result.write("t1 winer!!!!",font=('', 20, "bold"))
    result.goto(300, -120)
    result.write("t2 loser@#$%",font=('', 20, "bold"))
elif t1.pos()[0] < t2.pos()[0]:
    result.write("t2 winer!!!!",font=('', 20, "bold"))
    result.goto(300, -120)
    result.write("t1 loser@#$%",font=('', 20, "bold"))
else:
    result.write("t1 draw!",font=('', 20, "bold"))
    result.goto(300, -120)
    result.write("t2 draw!",font=('', 20, "bold"))

turtle.mainloop()