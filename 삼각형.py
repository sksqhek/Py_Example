import turtle
import random

turtle.setup(width=500, height=500)
t=turtle.Pen()
#t.pencolor("pink")
t.width(2)

colors = ["blue","green","black","red"]#색만들기
n = 0#색위치 설정할 변수

for i in range(0,370,12):
    t.pencolor(colors[n % len(colors)])#배열의 색을 하나씩 가져옴
    n += 1#다음 색으로
    t.forward(i)
    t.left(120)

