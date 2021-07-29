import time
from tkinter import*
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
id=canvas.create_oval(0, 100, 50, 150, fill="green")

def move_right(event):
    pos = canvas.coords(id)#원의 위치 얻어오기

    if pos[2] < 400:#원의 위치가 오른쪽 벽보다 작으면
        canvas.move(id, 5, 0)#움직이기

def move_left(event):
    pos = canvas.coords(id)

    if pos[0] > 0:
        canvas.move(id, -5, 0)

canvas.bind_all('<KeyPress-Right > ', move_right)
canvas.bind_all('<KeyPress-Left> ', move_left)

window.mainloop()