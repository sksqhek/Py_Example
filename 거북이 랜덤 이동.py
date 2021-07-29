from turtle import*
import random

class MyTurtle(Turtle):
    def glow(self, x ,y):
        #랜덤 색깔
        self.fillcolor(random.random(),random.random(),random.random())

        #랜덤 방향
        vec = random.randint(0,3)
        if vec == 0:
            self.setheading(0)
        if vec == 1:
            self.setheading(90)
        if vec == 2:
            self.setheading(180)
        if vec == 3:
            self.setheading(270)

        #이동
        self.forward(100)

        #화면을 벗어나면 되돌아 오기
        if self.pos()[0] < -(self.getscreen().window_width()/2) or self.pos()[0] > self.getscreen().window_width()/2:
            self.backward(100)
        if self.pos()[1] < -(self.getscreen().window_height()/2) or self.pos()[1] > self.getscreen().window_height()/2:
            self.backward(100)



t=MyTurtle()
t.shape("turtle")
t.onclick(t.glow)

mainloop()