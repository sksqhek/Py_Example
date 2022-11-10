import openpyxl
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

# 엑셀 파일 저장
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["건설 작업명", "작업 인원 수", "건설 작업 장소", "건설 작업 시간"])
# 엑셀 파일에 쓰기 위한 준비



# 사용자 입력
'''1. 건설작업 추가
2. 건설작업 검색
3. 건설작업 삭제
4.건설작업 전체 출력
5. 종료'''


def input_data():
    project_name = input("건설 작업 입력:")
    project_number = input("건설 작업 인력수 입력:")
    project_where = input("건설 작업 장소 입력:")
    project_time = input("건설 작업 시간 입력:")
    project_List.append({"project_name": project_name, "project_number": project_number, "project_where": project_where,
                         "project_time": project_time})
    sheet.append([project_name, project_number, project_where, project_time])
    global numOfData
    numOfData += 1


def search_data():
    search_name = input("검색할 작업 입력 >>>")
    is_find = False
    for data in project_List:
        if search_name == data["project_name"]:
            print("==========================")
            print("{}, {}, {}, {}".format(data["project_name"], data["project_number"], data["project_where"],
                                          data["project_time"]))
            print("==========================")
            is_find = True
    if not is_find:
        print("찾는 작업이 존재하지 않습니다.")


def delete_data():
    global numOfData
    delete_name = input("삭제할 작업 입력 >>>")
    is_find = False
    for data in project_List:
        if delete_name == data["project_name"]:
            project_List.remove(data)
            numOfData -= 1
            is_find = True
    if not is_find:
        print("삭제할 작업이 존재하지 않습니다.")


def show_all_data():
    # print(phoneList)
    print("총 {}개의 작업들이 있습니다.".format(numOfData))
    for data in project_List:
        print("==========================")
        print("{}, {}, {}, {}".format(data["project_name"], data["project_number"], data["project_where"],
                                      data["project_time"]))
        print("==========================")



print("==========================")
print("1. 건설작업 추가")
print("2. 건설작업 검색")
print("3. 건설작업 삭제")
print("4. 건설작업 전체 출력")
print("5. 종료")
print("==========================")

numOfData = 0
project_List = []
# f = open("./건설작업일정.txt", "r", encoding='UTF-8')
# data = f.readlines()
# for i in data:
#     i = i.strip()
#     i = i.split(",")
#     project_List.append({"project_name": i[0], "project_number": i[1], "project_where": i[2], "project_time": i[3]})

numOfData = len(project_List)

while True:
    menu = int(input("선택 >>> "))
    if menu == 1:
        input_data()
    elif menu == 2:
        search_data()
    elif menu == 3:
        delete_data()
    elif menu == 4:
        show_all_data()
    elif menu == 5:
        print("종료되었습니다.")
        f = open("./건설작업일정.txt", "w", encoding='UTF=8')
        for data in project_List:
            f.write(data["project_name"] + ',' + data["project_number"] + ',' + data["project_where"] + ',' + data[
                "project_time"] + '\n')
        f.close()
        break
    else:
        print("올바른 선택이 아닙니다.")

wb.save('현장작업목록.xlsx')

ui_file = './alarm.ui'
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file,self)

        self.pushButton.clicked.connect(self.buttonClick)

    def buttonClick(self):
        result = self.lineEdit.text()
        self.label.setText(result)

QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())

