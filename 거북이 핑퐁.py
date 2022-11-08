import turtle as t
import random
import time

def right():
    if player.xcor() < 200:
        player.forward(10)

def left():
    if player.xcor() > -200:
        player.backward(10)

t.bgcolor("Skyblue")
t.setup(500, 700)

player = t.Turtle()
player.shape("square")
player.shapesize(1, 5)
player.up()
player.speed(0)
player.goto(0, -270)

#ball
ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("white")

t.listen()
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")

ball_xspeed = 5
ball_yspeed = 5

game_on = True
life = 5
one = True

def yes():
    global life
    global  one

    one = True
    life = 5
    t.clear()
    t.goto(0, 300)
    t.write(f"life : {life}", False, "center", ("", 20))


def no():
    global game_on
    game_on = False

t.onkeypress(yes, "y")
t.onkeypress(no, "n")


#점수표시
t.up()
t.ht()
t.goto(0, 300)
t.write(f"life : {life}", False, "center", ("", 20))

while game_on:

    if life == 0:
        # game_on = False

        if one:#한번만 출력 되게
            t.goto(0, 0)
            t.write("Game Over", False, "center", ("", 20))
            t.goto(0, -25)
            t.write("restart y/n", False, "center", ("", 20))
            one = False
        else:
            t.goto(0, -25)
            t.write("", False, "center", ("", 20))

    else:
        new_x = ball.xcor() + ball_xspeed
        new_y = ball.ycor() + ball_yspeed
        ball.goto(new_x, new_y)

        if ball.xcor() > 240 or ball.xcor() < -240:
            ball_xspeed *= -1

        if ball.ycor() > 340:
            ball_yspeed *= -1

        if ball.ycor() < -340:
            life -= 1
            t.clear()
            t.goto(0, 300)
            t.write(f"life : {life}", False, "center", ("", 20))
            time.sleep(0.5)
            ball.goto(0, 100)
            ball_yspeed *= -1
            ball_xspeed *= -1

        if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
            ball_yspeed *= -1