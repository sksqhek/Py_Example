books=[]

def register():
    name = input("책제목 : ")
    ju = input("저자 : ")
    gab = input("가격 : ")
    books.append([name, ju,gab])

def book_list():
    for b in books:
        print(b)

while True:
    print("1.도서등록, 2.도서리스트, 3.대여하기, 4.대여리스트, 5.종료")
    cho = int(input("선택: "))
    if cho == 1:
        register()
    elif cho == 2:
        book_list()
    elif cho == 3:
        print()
    elif cho == 4:
        print()
    elif cho == 5:
        break
