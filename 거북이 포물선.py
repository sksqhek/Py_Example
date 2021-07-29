import turtle as t
import random


def turn_up():
    t.left(2)#각도 2도씩 증가


def turn_down():
    t.right(2)#각도 2도씩 감소


def fire():
    ang = t.heading()#시작 각도 저장
    while t.ycor() > 0:#지표면의 y위치가 0이기때문에 땅속으로 들어가면
        #밑에 2개를 반복
        t.forward(15)#15만큼 이동
        t.right(5)#아래로 5도

    d = t.distance(target, 0)#대포알이 땅속에 박힌후 목표물과의 거리 측정
    t.sety(random.randint(10, 100))#랜덤하게 글자 출력
    if d < 25:#25보다 작다면
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
    else:#25보다 크다면면
       t.color("red")
        t.write("Bad!", False, "center", ("", 15))

    #발사위치로 이동
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)#처음 시작 각도로

#지표면 그리기
t.goto(-300, 0)
t.down()
t.goto(300, 0)

#녹색 목표물 그리기
target = random.randint(50, 150)#랜덤 목표물 위치 생성
t.pensize(3)#선두께
t.color("green")
t.up()
t.goto(target - 25, 2)#목표물 위치를 기준으로 왼쪽으로 25만큼 이동
t.down()
t.goto(target + 25, 2)#오른족으로 25(도합 50크기)

#대포알 그리기
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)#대포알의 각도

#키 리스너 등록
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()

t.mainloop()