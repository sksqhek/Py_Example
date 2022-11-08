from tkinter import *
from tkinter import *
import time

window=Tk()

window.title("Physics")
window.geometry("640x600+100+100")
window.resizable(True, True)

canvas=Canvas(window, width=640, height=400, bg="white")
canvas.pack()

shapes = canvas.create_polygon(0, 375, 15, 375, 15, 375, 0, 375, fill="black")

def callback_mouse(event):
    print(event.x, event.y)
    global shapes
    canvas.delete(shapes)
    shapes = canvas.create_polygon(event.x, event.y, event.x+15, event.y, event.x+15, event.y+15, event.x, event.y+15, fill="black")
    for i in range(100):
        canvas.move(shapes, 0, scale.get()*i*0.05)
        window.update()
        time.sleep(0.05)

window.bind("<Button-1>", callback_mouse)

def select(self):
    value="중력 가속도 값 : "+str(scale.get())
    label.config(text=value)

var=IntVar()

scale=Scale(window, variable=var, command=select, orient="horizontal",  showvalue=True, tickinterval=5, to=100, length=300)
scale.pack()
label=Label(window,text="중력 가속도 값 : 0")
label.pack()

window.mainloop()