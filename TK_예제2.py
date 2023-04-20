from tkinter import *

## 정상적
window = Tk()
text = ['0','1','2','3','4','5']
class windows:
    def __init__(self):
        self.rab = []
        self.ab = IntVar()
        self.ab.set(0)
        for a in range(6):
            self.rab.append(Radiobutton(window, text=text[a], variable=self.ab, value=a, command=self.showvalue))
            self.rab[a].pack()
        window.mainloop()

    def showvalue(self):
        print(self.ab.get())


## 비정상적
class listwindow:
    def __init__(self, resolution, title, pictures, names, description):  # constructor
        imagesize = resolution.split('x')
        self.window = Tk()
        self.window.geometry(resolution)
        self.window.title(title)
        self.Pictures = pictures
        self.Pnames = names
        self.Pdescription = description
        self.currentP = IntVar()
        self.currentP.set(0)
        self.Image = PhotoImage(file=self.Pictures[self.currentP.get()], master=self.window)
        self.imagelabel = Label(self.window, image=self.Image, width=int(imagesize[0]) / 3 * 2,
                                height=int(imagesize[1]) - 300)
        self.descriptionlabel = Label(self.window, text=self.Pdescription[self.currentP.get()], font=('arial', 12), width=80, height=25)
        self.namelabel = Label(self.window, text=self.Pnames[self.currentP.get()], font=('arial', 17))
        self.quitbutton = Button(self.window, text="quit", font=('arial', 17), command=self.window.destroy)
        self.quitbutton.pack(side=BOTTOM)
        self.radlist = []

        for a in range(len(self.Pictures)):
            print(a)
            self.radlist.append(Radiobutton(self.window, text=self.Pnames[a], variable=self.currentP, value=a, command=self.describe))
            self.radlist[a].config(value=a)
            self.radlist[a].pack(side=BOTTOM)

        self.namelabel.pack(side=TOP)
        self.imagelabel.pack(side=TOP)
        self.descriptionlabel.pack(side=BOTTOM)

        self.window.mainloop()

    def describe(self):
        print("changing...", self.currentP.get())
        self.Image.config(file=self.Pictures[self.currentP.get()])
        self.imagelabel.config(image=self.Image)
        self.namelabel.config(text=self.Pnames[self.currentP.get()])
        self.imagelabel.update()
        self.namelabel.update()
        self.descriptionlabel.config(text=self.Pdescription[self.currentP.get()])
        self.descriptionlabel.update()

    def update(self):
        for a in range(len(self.radlist)):
            self.radlist[a].config(value=3)
            self.radlist[a].update()

windows()
listwindow("500x500", "title", ["1.gif"], ["name"], ["descrip"])