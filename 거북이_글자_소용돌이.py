import turtle
import random
from tkinter.simpledialog import *
import math

## 전역 변수 선언 부분 ##

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0, 0, 20
radius, angle, radian = 1, 180, 0

## 메인 코드 부분 ##
turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=500, height=500)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
angle = 360 / len(inStr)  # 문자열의 길이로 각도 설정

for ch in inStr:
    radian = 3.14 * angle / 180
    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)

    r = random.random()
    g = random.random()
    b = random.random()

    turtle.goto(tX, tY)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

    angle -= 360 / len(inStr)  # 각도만큼 반시계로 회전
    radius += 5

turtle.done()