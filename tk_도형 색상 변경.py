from tkinter import *
import time
import random

window = Tk()

canvas = Canvas(window, width=600, height=400)
canvas.pack()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

mycolor = random.choice(colors)


class Ball():
    def __init__(self, color, size):
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.dx = random.randint(1, 10)
        self.dy = random.randint(1, 10)

    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0:
            mycolor = random.choice(colors)
            canvas.itemconfig(self.id , fill=mycolor)#색 변경
            self.dy = -self.dy

        if x1 > canvas.winfo_width() or x0 < 0:
            mycolor = random.choice(colors)
            canvas.itemconfig(self.id, fill=mycolor)#색 변경
            self.dx = -self.dx


ball1 = Ball(mycolor, 60)
ball2 = Ball(mycolor, 60)
ball3 = Ball(mycolor, 60)
ball4 = Ball(mycolor, 60)
ball5 = Ball(mycolor, 60)

while True:
    ball1.move()
    ball2.move()
    ball3.move()
    ball4.move()
    ball5.move()
    window.update()
    time.sleep(0.05)
window.mainloop()