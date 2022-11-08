import turtle as t
t.left(270)
t.speed(0)
color = ['red','orange','yellow','green','blue','magenta', 'purple']

for i in range(7, 0, -1):
    t.color(color[i-1])
    t.penup()
    r = 100*i
    t.goto(0,0)
    t.goto(r / 2 * -1, 0)
    t.pendown()
    t.begin_fill()
    t.circle(r / 2, -180)
    t.end_fill()
    t.left(180)

t.done()
