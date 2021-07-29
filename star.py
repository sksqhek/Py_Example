import turtle
import random
from turtle import width

t = turtle.Turtle()

t.speed(0)
t.penup()

turtle.bgcolor("black")
turtle.colormode(255)

width = turtle.Screen().window_width()
height = turtle.Screen().window_height()#화면이 크기 얻어오기


def draw():
    size = random.randint(10, 200)#별의 크기
    x = random.randint(-width/2 + size, width/2 - size)
    y = random.randint(-height/2 + size, height/2 - size)#별의 위치
    t.goto(x,y)

    cR = random.randint(0, 255)
    cG = random.randint(0, 255)
    cB = random.randint(0, 255)
    t.color(cR,cG,cB)

    t.begin_fill()
    for i in range(5):
        t.forward(size)#사이즈 만큼 이동
        t.right(144)
    t.end_fill()


while True:
    draw()

turtle.mainloop()