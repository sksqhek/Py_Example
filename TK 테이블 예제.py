from random import randint, random, shuffle
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
from IPython.display import display

table = []#위젯
table_data = []#데이터

cnt = 0

def donothing():
    filewin = Toplevel(window)  # 새로운 창 띄우기
    Button(filewin, text="Do nothing button").pack()


def openFile():
    #global fname
    fname = askopenfilename(filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    #messagebox.showinfo('You choosed:', fname)
    loadData(fname)

def addTable(data):
    global cnt
    if data[0] == None:
        return
    table[int(cnt / 5)][cnt % 5].delete(0,"end")
    table[int(cnt / 5)][cnt % 5].insert(0, "%.0f %.0f %s" % (data[0], data[1], data[2]))
    cnt += 1

def loadData(fname):
    global cnt

    df_csv = pd.read_csv(fname)
    display(df_csv)

    table_data.clear()
    cnt = 0
    idx = 0
    for value in df_csv.values:
        addTable(value)
        table_data.append(value)#리스트에 데이터 저장

def new():
    idx = 0;
    for line in table_data:
        table[int(idx / 5)][idx % 5].delete(0, "end")
        idx += 1
    table_data.clear()

window = Tk()
window.title("My Project")

# Menu 생성하기
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

editmenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

helpmenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)

window.config(menu=menubar)

# Label 생성하기
Label(window, text="좌석표").grid(row=2, column=0, columnspan=2)

def createTable(row, col):# Entry table 생성하기
    for i in range(row):  # Rows
        t = []
        for j in range(col):  # Columns
            b = Entry(window, text="")
            b.grid(row=i + 3, column=j)
            t.append(b)
        table.append(t)


def reLocation():#재배치
    shuffle(table_data)#섞기

    idx = 0;
    for line in table_data:
        table[int(idx/5)][idx%5].delete(0, "end")
        table[int(idx/5)][idx%5].insert(0, "%.0f %.0f %s"%(line[0],line[1],line[2]))
        idx += 1


re_button = Button(window, text="재배치", command=reLocation)
re_button.grid(row=13, column=1)

createTable(6,5);

loadData("Information.csv")

window.mainloop()