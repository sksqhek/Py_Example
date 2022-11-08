# tkinter 모듈 불러오기--------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox

# 메뉴 딕셔너리 만들기 --------------------------------------------------------------------------------------
hco = {0: "에스프레소", 1: "아메리카노", 2: "카페라떼", 3: "카푸치노", 4: "카페모카", 5: "카라멜 마끼아또", 6: "헤이즐넛 라떼", 7: "바닐라 라떼", 8: "연유 라떼",
       9: "달고나 크림라떼", 10: "흑임자 카페라떼", 11: "아포카토"}
ico = {0: "아메리카노", 1: "카페라떼", 2: "카페모카", 3: "카라멜 마끼아또", 4: "헤이즐넛 라떼", 5: "바닐라 라떼", 6: "달고나 라떼", 7: "블루오션 라떼",
       8: "그린오션 라떼"}
nco = {0: "초코", 1: "녹차", 2: "고구마", 3: "인절미", 4: "자색고구마", 5: "딸기", 6: "달고나", 7: "민트초코", 8: "밀크티", 9: "흑임자"}
ade = {0: "레몬", 1: "복숭아", 2: "자몽", 3: "라임", 4: "청귤", 5: "블루레몬", 6: "메론", 7: "귤", 8: "사과"}
smo = {0: "딸기", 1: "블루베리", 2: "복숭아", 3: "망고", 4: "홍시", 5: "귤"}
sha = {0: "커피", 1: "바닐라", 2: "초코", 3: "딸기", 4: "홍시", 5: "쿠앤크", 6: "망고", 7: "복숭아", 8: "블루베리", 9: "오레오", 10: "밀크",
       11: "자두", 12: "레몬"}
tea = {0: "레몬", 1: "라임", 2: "귤", 3: "청귤", 4: "자몽", 5: "얼그레이"}
ice = {0: "바닐라 아이스크림", 1: "딸기 아이스크림", 2: "초코 아이스크림", 3: "블루베리 아이스크림", 4: "망고 아이스크림", 5: "딸기 프라페", 6: "인절미 빙수",
       7: "녹차 빙수", 8: "초코 빙수", 9: "베리 빙수", 10: "망고 빙수", 11: "흑임자 빙수", 12: "민트초코 빙수", 13: "치즈케익 빙수"}
bre = {0: "플레인 와플", 1: "크림치즈 와플", 2: "블루베리 와플", 3: "딸기 와플", 4: "바닐라아이스크림 와플", 5: "딸기아이스크림 와플", 6: "녹차아이스크림 와플",
       7: "치즈 스모어쿠키", 8: "초코 스모어쿠키",
       9: "딸기 스모어쿠키", 10: "녹차 스모어쿠키", 11: "모카 스모어쿠키", 12: "쿠앤크 스모어쿠키", 13: "허니브레드", 14: "초코 허니브레드"}
checkclk = {}
order = []


# 메뉴판으로 넘어가기 -------------------------------------------------------------------------------------
def next():
    frame1.pack_forget()
    frame2.pack(anchor="n", fill="both", expand=True)
    frame12.pack(side="bottom", fill="both", expand=True)
    frame3.pack(anchor="n", fill="both", ipady=310, expand=True)


# 각 메뉴판 프레임 함수 -------------------------------------------------------------------------------------
def menu3():
    frame3.pack(anchor="n", fill="both", ipady=310, expand=True)
    for i in range(4, 12):
        eval(f"frame{i}.pack_forget()")


def menu4():
    frame3.pack_forget()
    for i in range(5, 12):
        eval(f"frame{i}.pack_forget()")
    frame4.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu5():
    for i in range(3, 5):
        eval(f"frame{i}.pack_forget()")
    for i in range(6, 12):
        eval(f"frame{i}.pack_forget()")
    frame5.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu6():
    for i in range(3, 6):
        eval(f"frame{i}.pack_forget()")
    for i in range(7, 12):
        eval(f"frame{i}.pack_forget()")
    frame6.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu7():
    for i in range(3, 7):
        eval(f"frame{i}.pack_forget()")
    for i in range(8, 12):
        eval(f"frame{i}.pack_forget()")
    frame7.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu8():
    for i in range(3, 8):
        eval(f"frame{i}.pack_forget()")
    for i in range(9, 12):
        eval(f"frame{i}.pack_forget()")
    frame8.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu9():
    for i in range(3, 9):
        eval(f"frame{i}.pack_forget()")
    for i in range(10, 12):
        eval(f"frame{i}.pack_forget()")
    frame9.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu10():
    for i in range(3, 10):
        eval(f"frame{i}.pack_forget()")
    frame11.pack_forget()
    frame10.pack(anchor="n", fill="both", ipady=310, expand=True)


def menu11():
    for i in range(3, 11):
        eval(f"frame{i}.pack_forget()")
    frame11.pack(anchor="n", fill="both", ipady=310, expand=True)


# extra 추가하기 ---------------------------------------------------------------------------------------
def add(item):
    order.append(item)
    order_label.insert(frame13, text=item, font=("나눔손글씨 펜", 33))
    order_label.pack()

    def ok():
        user_choice = ""
        for i in check_value:
            if check_value[i].get():
                user_choice += extra[i] + ', '
                check_value[i].set(False)
        checklabel = Label(frame12, text=f"{user_choice} 완료", font=("나눔손글씨 펜", 33))
        checklabel.grid(column=1, row=1)
        extra_win.destroy()

    extra_win = Tk()
    extra_win.title("extra 선택")
    extra_win.geometry("350x430")
    extra_label = Label(extra_win, text="extra 선택", font=("나눔손글씨 펜", 45), fg="brown")
    extra_label.grid(column=0, row=0, ipadx=90, ipady=20)
    extra = {0: "샷 추가", 1: "시럽 추가", 2: "펄 추가", 3: "사이즈 업"}
    check_value = {}
    for i in range(len(extra)):
        check_value[i] = BooleanVar()
        extrabtn = Checkbutton(extra_win, text=extra[i], variable=check_value[i], font=("나눔손글씨 펜", 33))
        extrabtn.grid(column=0, row=i + 2)
    okbutton = Button(extra_win, text="담기", font=("나눔손글씨 펜", 36), command=ok)
    okbutton.grid(column=0, row=6, ipadx=15, pady=22)
    extra_win.mainloop()


# 주문 완료하기 -----------------------------------------------------------------------------------------
def order():
    for i in range(2, 13):
        eval(f"frame{i}.pack_forget()")
    frame13.pack(anchor="center", expand=True)
    order_laber1 = Label(frame13, text="주문하신""\n나왔습니다!", font=("나눔손글씨 펜", 50), fg="brown")
    order_laber2 = Label(frame13, text="오픈 기념으로 무료예요ㅎㅎ \n맛있게 드세요!!", font=("나눔손글씨 펜", 30), fg="brown")
    order_laber1.pack()
    order_laber2.pack()


# 윈도우 불러오기 -----------------------------------------------------------------------------------------
win = Tk()
win.title("IMAGE CAFE")
win.geometry("2560x1024")
win.resizable(width=False, height=False)

# 프레임1: 첫 화면 만들기 -----------------------------------------------------------------------------------
frame1 = Frame(win)
frame1.pack(anchor="center", expand=True)
main1 = Label(frame1, text="~* Leemage CAFE *~", font=("나눔손글씨 펜", 88), fg="brown")
main2 = Label(frame1, text="~눈으로 먹는 이미지 카페~", font=("나눔손글씨 펜", 48), fg="brown")
button = Button(frame1, text="주문하기", font=("나눔손글씨 펜", 40), width=10, height=2, command=next)
main1.pack()
main2.pack()
button.pack(pady=50)

# 프레임2: 메뉴 종류 버튼 만들기 ------------------------------------------------------------------------------
frame2 = Frame(win, relief="groove", bd=2)
select = Label(frame2, text="메뉴를 선택하세요!", fg="brown", font=("나눔손글씨 펜", 42))
select.grid(column=1, row=0, columnspan=9, ipady=15)

btn1 = Button(frame2, text="핫 커피", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu3)
btn2 = Button(frame2, text="아이스 커피", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu4)
btn3 = Button(frame2, text="논 커피", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu5)
btn4 = Button(frame2, text="에이드", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu6)
btn5 = Button(frame2, text="스무디", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu7)
btn6 = Button(frame2, text="쉐이크", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu8)
btn7 = Button(frame2, text="티", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu9)
btn8 = Button(frame2, text="아이스크림", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu10)
btn9 = Button(frame2, text="디저트", font=("나눔손글씨 펜", 20), width=11, height=2, command=menu11)
for i in range(1, 10):
    eval(f"btn{i}.grid(column=i, row=1)")

# 메뉴 프레임(3,4,5,6,7,8,9,10,11) 설정 ---------------------------------------------------------------------
frame3 = Frame(win, relief="groove", bd=2)
frame4 = Frame(win, relief="groove", bd=2)
frame5 = Frame(win, relief="groove", bd=2)
frame6 = Frame(win, relief="groove", bd=2)
frame7 = Frame(win, relief="groove", bd=2)
frame8 = Frame(win, relief="groove", bd=2)
frame9 = Frame(win, relief="groove", bd=2)
frame10 = Frame(win, relief="groove", bd=2)
frame11 = Frame(win, relief="groove", bd=2)
frame13 = Frame(win)

# 메뉴 프레임에 맞는 음료 띄우기--------------------------------------------------------------------------------
for i in range(len(hco)):
    hcobox = Button(frame3, text=hco[i], font=("나눔손글씨 펜", 30), command=lambda: add(hco[i]))
    if (i < 6):
        hcobox.grid(column=1, row=i, padx=290, pady=15, ipadx=10, ipady=7)
    elif (5 < i):
        hcobox.grid(column=6, row=11 - i, pady=15, ipadx=10, ipady=7)
for i in range(len(ico)):
    icobox = Button(frame4, text="아이스 " + ico[i], font=("나눔손글씨 펜", 30), command=lambda: add(ico[i]))
    if (i < 5):
        icobox.grid(column=1, row=i, padx=255, pady=15, ipadx=10, ipady=8)
    elif (4 < i):
        icobox.grid(column=2, row=8 - i, pady=15, ipadx=10, ipady=8)
for i in range(len(nco)):
    ncobox = Button(frame5, text=nco[i] + " 라떼", font=("나눔손글씨 펜", 30), command=lambda: add(nco[i]))
    if (i < 5):
        ncobox.grid(column=1, row=i, padx=290, pady=15, ipadx=10, ipady=8)
    elif (4 < i):
        ncobox.grid(column=2, row=9 - i, pady=15, ipadx=10, ipady=8)
for i in range(len(ade)):
    adebox = Button(frame6, text=ade[i] + " 에이드", font=("나눔손글씨 펜", 30), command=lambda: add(ade[i]))
    if (i < 5):
        adebox.grid(column=1, row=i, padx=320, pady=12, ipadx=10, ipady=8)
    elif (4 < i):
        adebox.grid(column=2, row=8 - i, pady=12, ipadx=10, ipady=8)
for i in range(len(smo)):
    smobox = Button(frame7, text=smo[i] + " 스무디", font=("나눔손글씨 펜", 30), command=lambda: add(smo[i]))
    smobox.grid(column=1, row=i, padx=542, pady=12, ipadx=10, ipady=8)
for i in range(len(sha)):
    shabox = Button(frame8, text=sha[i] + " 쉐이크", font=("나눔손글씨 펜", 30), command=lambda: add(sha[i]))
    if (i < 4):
        shabox.grid(column=1, row=i, padx=197, pady=12, ipadx=10, ipady=8)
    elif (3 < i < 9):
        shabox.grid(column=2, row=8 - i, pady=12, ipadx=10, ipady=8)
    elif (8 < i):
        shabox.grid(column=3, row=12 - i, padx=197, pady=12, ipadx=10, ipady=8)
for i in range(len(tea)):
    teabox = Button(frame9, text=tea[i] + " 티", font=("나눔손글씨 펜", 30), command=lambda: add(tea[i]))
    teabox.grid(column=1, row=i, padx=555, pady=12, ipadx=10, ipady=8)
for i in range(len(ice)):
    icebox = Button(frame10, text=ice[i], font=("나눔손글씨 펜", 30), command=lambda: add(ice[i]))
    if (i < 5):
        icebox.grid(column=1, row=i, padx=185, pady=12, ipadx=10, ipady=8)
    elif (4 < i < 9):
        icebox.grid(column=2, row=8 - i, pady=15, ipadx=10, ipady=8)
    elif (8 < i):
        icebox.grid(column=3, row=13 - i, padx=185, pady=12, ipadx=10, ipady=8)
for i in range(len(bre)):
    brebox = Button(frame11, text=bre[i], font=("나눔손글씨 펜", 30), command=lambda: add(bre[i]))
    if (i < 5):
        brebox.grid(column=1, row=i, padx=157, pady=12, ipadx=10, ipady=8)
    elif (4 < i < 10):
        brebox.grid(column=2, row=9 - i, pady=12, ipadx=10, ipady=8)
    elif (9 < i):
        brebox.grid(column=3, row=14 - i, padx=157, pady=12, ipadx=10, ipady=8)

# 메뉴 프레임에 주문하기 버튼 만들기 ----------------------------------------------------------------------------
frame12 = Frame(win, relief="groove", bd=2)
choicebtn = Button(frame12, text="주문하기", font=("나눔손글씨 펜", 40), command=order)
choicebtn.grid(column=2, row=1, padx=50, pady=20, ipadx=10, ipady=7)

win.mainloop()