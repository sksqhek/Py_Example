# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()
t.shape("turtle")

colorlist = ["green", "yellow", "red", "purple", "blue", "orange"]


def basis_back(n, length):
    global color
    for k in range(n - 1):
        t.fillcolor(colorlist[color])
        t.begin_fill()
        for r in range(n - 4):
            for i in range(n):
                t.fd(length)
                t.right(60)
            t.left(120)
        t.end_fill()
        color += 1
        if (color >= len(colorlist)):
            color = 0
        t.fd(length)
        t.left(60)
        t.fd(length)
        t.left(60)
        t.fd(length)
        t.left(60)


def inside_back(n, a):
    for r in range(n):
        for m in range(3):
            t.penup()
            t.fd(2 * a)
            t.pendown()
            t.right(60)
        basis_back(n, a)
        t.penup()
        t.fd(2 * length)
        t.pendown()
        t.left(60)


print("지금부터 당신만의 무지개 거북이를 만들어 봐요!")
print("먼저 크기를 골라볼까요?")
print("1. 완전 쪼꼬미라서 귀여웡.")
print("2. 쪼꼬미라서 인 마이 포켓.")
print("3. 중간 사이즈도 사랑스러워.")
print("4. 넌 나만의 조금 큰 거북이!")
print("5. 인간크기 만한 베스트 프랜드 거북.")
size = input("당신이 원하는 거북이의 크기는? :")

if (size == 1):
    length = 30

elif (size == 2):
    length = 60

elif (size == 3):
    length = 90

elif (size == 4):
    length = 120

else:
    length = 150

t.width(3)
color = 0
basis_back(6, length)
a = float(length / 5)
t.width(1)
inside_back(6, a)
print("배경 색깔을 골라볼까요?")
background = input("원하는 배경 색깔을 영어로 입력하세요.")
turtle.bgcolor(background)
turtle.done()