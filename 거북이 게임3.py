import turtle
import math

player = turtle.Turtle()
player.shape('turtle')
screen=player.getscreen()

goal = turtle.Turtle()
goal.penup()
goal.goto(300,-250)
goal.pendown()
goal.left(90)
goal.pensize(10)
goal.forward(600)

txt_score = turtle.Turtle()
txt_score.color("green")
txt_score.penup()
txt_score.speed(0)
txt_score.hideturtle()

def turnleft():
    player.left(5)
def turnright():
    player.right(5)

def fire():
    x=0
    y=0
    velocity=50
    angle=player.heading()
    vx=velocity*math.cos(angle*3.14/180)
    vy=velocity*math.cos(angle*3.14/180)

    while player.ycor()>=0:
        vx=vx
        vy=vy-10
        x=x + vx
        y=y + vy
        player.goto(x,y)

        if int(goal.pos()[0]) <= int(player.pos()[0]):#x좌표가 같거나 크다면면
           txt_score.goto(player.pos()[0], player.pos()[1])
           txt_score.write("goal!", font=('', 20, "bold"))

screen.onkeypress(turnleft,'Left')
screen.onkeypress(turnright,'Right')
screen.onkeypress(fire,'space')
screen.listen()

screen.mainloop()
