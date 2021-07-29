import turtle as t
import random
import math

t.setup(500, 500)
t.bgcolor("black")

t1 = t.Turtle()
t1.color("blue")
t1.shape("turtle")
t1.speed(0)
t1.penup()
screen = t1.getscreen()

score = [0]
t2 = t.Turtle()
t2.color("white")
t2.penup()
t2.goto(0, 200)
t2.write("Score : %d" % score[0], font=('', 20, "bold"))
t2.hideturtle()

asteroids = []

asteroids_no = 10


def addAsteroid():
    a1 = t.Turtle()

    a1.type = random.randint(0,1)#1이면 보석 0이면 폭탄
    if a1.type == 1:
        a1.color("red")
        a1.shape("circle")
    else:
        a1.color("orange")
        a1.shape("triangle")

    a1.penup()
    a1.speed(10)
    a1.goto(random.randint(-250, 250), random.randint(-250, 250))
    a1.vec = [random.randint(-10, 10), random.randint(-10, 10)]  # 움직이는 속도
    asteroids.append(a1)


for i in range(asteroids_no):
    addAsteroid()


def turn_right():
    t1.setheading(0)


def turn_up():
    t1.setheading(90)


def turn_left():
    t1.setheading(180)


def turn_down():
    t1.setheading(270)


def turn_space():
    t1.fd(100)


t.onkeypress(turn_right, "Right")  # 방향키 오른쪽 화살표
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_space, "space")
screen.listen()


def play():
    width = t.getscreen().window_width() / 2
    height = t.getscreen().window_height() / 2

    t1.forward(10)

    if -width > t1.pos()[0] or width < t1.pos()[0]:
        t1.backward(20)
    if -height > t1.pos()[1] or height < t1.pos()[1]:
        t1.backward(20)

    for a in asteroids:
        # a.right(random.randint(-180, 180))
        # a.fd(5)
        a.goto(a.pos()[0] + a.vec[0], a.pos()[1] + a.vec[1])
        if -width > a.pos()[0] or width < a.pos()[0]:
            a.vec[0] *= -1
        if -height > a.pos()[1] or height < a.pos()[1]:
            a.vec[1] *= -1

        if t1.distance(a.pos()) < 20:  # 충돌할 경우
            asteroids.remove(a)  # 리스트에서 삭제
            a.hideturtle()  # 않보이게

            if a.type == 1:#타입에 맞쳐서 점수 적용
                score[0] += 1
            else:
                score[0] -= 1

            del a

            t2.clear()
            t2.write("Score : %d" % score[0], font=('', 20, "bold"))
            for b in asteroids:  # 충돌할때 마다 1%씩 속도 증가
                b.vec[0] *= 1.1
                b.vec[1] *= 1.1

    screen.ontimer(play, 10)


screen.ontimer(play, 10)

t.mainloop()