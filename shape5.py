import turtle
import random

t = turtle.Pen()

def penta():
    for i in range(5):
        t.forward(100)
        t.left(360/5)#오각형은 이렇게 

penta()#함수 실행

turtle.mainloop()