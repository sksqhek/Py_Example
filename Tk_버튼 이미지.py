from tkinter import *
import PIL

root = Tk()
root.title("GUI")

photo = PhotoImage(file="fire.png")

#image = PIL.Image.open("농사.png")
#photo = PIL.ImageTk.PhotoImage(image)

btn6 = Button(root, image=photo)
btn6.pack()

root.mainloop()