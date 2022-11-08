from tkinter import *
window = Tk()

number = 0

def quit():
    sys.exit(0)

def Up():
    global number
    number += 1
    label.config(text=str(number))

def Down():
    global number
    number -= 1
    label.config(text=str(number))

button1 = Button(window, text="파이썬 종료",fg="red",command=quit)
button2 = Button(window, text = "Up",command=Up)
button3 = Button(window, text = "Down",command=Down)
label = Label(window, text=str(number))

label.pack()
button2.pack()
button3.pack()
button1.pack()

window.mainloop()