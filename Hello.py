import turtle
import random

t = turtle.Pen()
t.shape("turtle")
t.shapesize(3,3)
t.up()

t2 = turtle.Pen()
t2.up()
score = [0]

t2.goto(-200,380)#점수 출력
t2.write('score:%d'%score[0],font=('Arial', 20, "bold"))

def show(x,y):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    t.goto(x,y)

    score[0] += 1#점수 증가
    t2.goto(-200,380)#점수 출력
    t2.clear()
    t2.write('score:%d'%score[0],font=('Arial', 20, "bold"))


t.onclick(show)

turtle.mainloop()

