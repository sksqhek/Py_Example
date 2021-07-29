from tkinter import *
from tkinter import filedialog



class Book:
    def __init__(self, title, writer, publish):
        #"""인스턴스 변수 설정"""
        self.title = title
        self.writer = writer
        self.publish = publish


class Book_rental(Book):

    def __init__(self, number, title, writer, publish, name):
        super().__init__(title, writer, publish)
        self.number = number
        self.name = name


book_rental_list = []
current_index = [0]#화면에 보여지는 리스트의위치


def set_Text():#화면에 출력(current_index로 )

    if len(book_rental_list) == 0:
        return

    number.set(book_rental_list[current_index[0]].number)
    title.set(book_rental_list[current_index[0]].title)
    writer.set(book_rental_list[current_index[0]].writer)
    publish.set(book_rental_list[current_index[0]].publish)
    name.set(book_rental_list[current_index[0]].name)

def open():
    file = filedialog.askopenfile(parent=w, mode='r')

    book_rental_list.clear()
    idx = 0;
    for line in file.readlines():#파일에서 한줄씩 읽기
        read = line.split()#공백 문자를 기준으로 데이터 분리
        data = Book_rental(read[0],read[1],read[2],read[3],read[4])#객체 생성
        book_rental_list.append(data)#만들어진 객체를 리스트에 저장
        idx += 1

    current_index[0] = idx - 1
    set_Text()

    file.close()

def save():
    file = filedialog.asksaveasfile(parent=w, mode='w')

    for r in book_rental_list:#리스트에 저장된 내용을 파일에 저장
        file.write("%s %s %s %s %s\n"%(r.number,r.title,r.writer,r.publish,r.name))
    file.close()


def add_list():
    data = Book_rental(number.get(), title.get(), writer.get(), publish.get(), name.get())

    book_rental_list.append(data)#입력된 데이터로 만든 객체를 리스트에 저장

    current_index[0] = len(book_rental_list) - 1

    print(data.number)


def to_first():
    current_index[0] = 0#출력 위치를 0으로
    set_Text()

def to_befort():
    current_index[0] -= 1
    if current_index[0] < 0:#범위를 벗어나면
        current_index[0] = 0

    set_Text()

def to_next():
    current_index[0] += 1
    if current_index[0] > len(book_rental_list) - 1:#범위를 벗어나면
        current_index[0] = len(book_rental_list) - 1
    set_Text()

def to_last():
    current_index[0] = len(book_rental_list) - 1#출력 위치를 마지막으로
    set_Text()

w = Tk()
w.title('도서대출')
f = Frame(w)
f.pack()

menu = Menu(w)
w.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장하기", command=save)
filemenu.add_command(label="종료", command=w.destroy)

lbnumber = Label(f, text='번  호')
lbnumber.grid(row=1, column=1)
number= StringVar()
ennumber = Entry(f, textvariable=number, width=30)
ennumber.grid(row=1, column=2, columnspan=10)


lbtitle = Label(f, text='제  목')
lbtitle.grid(row=2, column=1)
title = StringVar()
entitle = Entry(f, textvariable=title, width=30)
entitle.grid(row=2, column=2)

lbwriter = Label(f, text='저  자')
lbwriter.grid(row=3, column=1)
writer = StringVar()
enwriter = Entry(f, textvariable=writer, width=30)
enwriter.grid(row=3, column=2)

lbpublish = Label(f, text='출판사')
lbpublish.grid(row=4, column=1)
publish = StringVar()
enpublish = Entry(f, textvariable=publish, width=30)
enpublish.grid(row=4, column=2)

lbname = Label(f, text='대출인')
lbname.grid(row=5, column=1)
name = StringVar()
enname = Entry(f, textvariable=name, width=30)
enname.grid(row=5, column=2)

bt1 = Button(f, text='추가', command=add_list)
bt1.place(x=35, y=105)
bt2 = Button(f, text='처음', command=to_first)
bt2.place(x=75, y=105)
bt3 = Button(f, text='다음', command=to_next)
bt3.place(x=115, y=105)
bt4 = Button(f, text='이전', command=to_befort)
bt4.place(x=155, y=105)
bt5 = Button(f, text='마지막', command=to_last)
bt5.place(x=195, y=105)

message = Message(f)
message.grid(row=7, column=1)

w.mainloop()