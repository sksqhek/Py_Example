from turtle import*

def drawStar(x,y):
    goto(x-50,y+25)#마우스 위치로 이동

    pendown()
    for i in range(5):
        forward(100)
        right(144)
    penup()

penup()

onscreenclick(drawStar, 1)#마우스를 누루면 drawStar함수 실행
listen()

done()