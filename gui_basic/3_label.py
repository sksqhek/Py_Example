from tkinter import *

root = Tk()
root.title("Nado GUI")

label1 = Label(root, text='Hi World!!!')
label1.pack()

photo = PhotoImage(file='img.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    global photo
    label1.config(text='또 만나요!!!!!!')

    photo = PhotoImage(file='img2.png')
    label2.config(image=photo)

btn = Button(root, text='Click', command=change)
btn.pack()

root.mainloop()