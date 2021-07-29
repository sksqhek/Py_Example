import turtle
from tkinter.colorchooser import askcolor

screen = turtle.Turtle()
screen.hideturtle()
screen.penup()
screen.speed(0)
key = screen.getscreen()

currShape = [0]#현재 그리고 있는 도형
isFill = [True]#색이 차있는 도형 인지

def drawShape(n, fill):
    currShape[0] = n#도형 모양 저장
    isFill[0] = fill#색을 저장

    screen.clear()
    screen.pendown()

    if fill:#상태가 색채우기 일때만
        screen.begin_fill()

    for i in range(n):
        screen.left(360/n)
        screen.forward(100)

    if fill:
        screen.end_fill()

    screen.penup()

def selectColor():
    color = askcolor()#색 얻어오기
    screen.color(color[1])#색지정

    if currShape[0] != 0:#도형을 그릴때만
        drawShape(currShape[0], isFill[0])#색을 적용해서 다시 그리기


def selectShape1():
    drawShape(3 ,True)
def selectShape2():
    drawShape(4,True)
def selectShape3():
    drawShape(5,True)
def selectShape4():
    drawShape(6,True)

def backDelete():#도형 안이 비게 만들기
    drawShape(currShape[0], False)

def allDelete():
    currShape[0] = 0
    screen.clear()



key.onkeypress(selectColor, "c")
key.onkeypress(selectShape1, "3")
key.onkeypress(selectShape2, "4")
key.onkeypress(selectShape3, "5")
key.onkeypress(selectShape4, "6")
key.onkeypress(backDelete, "d")
key.onkeypress(allDelete, "r")
key.listen()


turtle.mainloop()