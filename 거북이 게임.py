import turtle
import random
import math

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen = player.getscreen()

score = [0]
txt_score = turtle.Turtle()
txt_score.color("green")
txt_score.penup()
txt_score.speed(0)
txt_score.goto(0, 400)
txt_score.write("Score : %d" % score[0], font=('', 20, "bold"))
txt_score.hideturtle()

asteroids = []

asteroids_no = 10

def addAsteroid():
    a1 = turtle.Turtle()
    a1.color("red")
    a1.shape("circle")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300, 300), random.randint(-300, 300))
    a1.vec = [random.randint(-10, 10), random.randint(-10, 10)]#움직이는 속도
    asteroids.append(a1)

for i in range(asteroids_no):
    addAsteroid()

def turnleft():
        player.left(30)

def turnright():
        player.right(30)

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

def play():
        width = turtle.getscreen().window_width() / 2
        height = turtle.getscreen().window_height() / 2

        player.forward(2)#플레이어가 벽에 붙이치면
        if -width > player.pos()[0] or width < player.pos()[0]:
            player.backward(20)
        if -height > player.pos()[1] or height < player.pos()[1]:
            player.backward(20)

        for a in asteroids:
            #a.right(random.randint(-180, 180))
            #a.fd(5)
            a.goto(a.pos()[0] + a.vec[0], a.pos()[1] + a.vec[1] )
            if -width > a.pos()[0] or width < a.pos()[0]:
                a.vec[0] *= -1
            if -height > a.pos()[1] or height < a.pos()[1]:
                a.vec[1] *= -1


            if player.distance(a.pos()) < 20:#충돌할 경우
                asteroids.remove(a)#리스트에서 삭제
                a.hideturtle()  # 않보이게
                del a
                addAsteroid()#새로운 별동별 생성
                score[0] += 1
                txt_score.clear()
                txt_score.write("Score : %d" % score[0], font=('', 20, "bold"))
                for b in asteroids:#충돌할때 마다 1%씩 속도 증가
                    b.vec[0] *= 1.1
                    b.vec[1] *= 1.1


        screen.ontimer(play, 10)
screen.ontimer(play, 10)

turtle.mainloop()