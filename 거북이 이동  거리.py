import turtle as t
t.shape("turtle")
te=t.Turtle()
te.shape("classic")

pos = [-200, 0]
t.goto(pos)

while True:
    pos[0] += 1
    t.goto(pos)#왼쪽에서 오른쪽으로 이동

    if t.distance(te.pos()) < 50:#50보다 작으면
        te.hideturtle()
    else:
        te.showturtle()

    if pos[0] > 200:#x위치가 200보다 크면 반복 종료
        break

t.mainloop()