import sys
from PyQt5.QtWidgets import *
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.pushButton1 = QPushButton(self)
        self.pushButton1.setText('과거파일 열기')
        self.pushButton1.clicked.connect(self.pushButtonClicked1)

        self.pushButton2 = QPushButton(self)
        self.pushButton2.setText('현재파일 열기')
        self.pushButton2.clicked.connect(self.pushButtonClicked2)

        self.pushButton3 = QPushButton(self)
        self.pushButton3.setText('추출하기')
        self.pushButton3.clicked.connect(self.compare_excel)

        self.label1 = QLabel(self)
        self.label1.setText("파일 경로1")

        self.label2 = QLabel(self)
        self.label2.setText("파일 경로2")

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.label1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.label2)
        layout.addWidget(self.pushButton3)

        self.setLayout(layout)

        self.setGeometry(800, 300, 500, 300)
        self.setWindowTitle('ExcelCompare')

    def pushButtonClicked1(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label1.setText(fname[0])

    def pushButtonClicked2(self):
        fname1 = QFileDialog.getOpenFileName(self)
        self.label2.setText(fname1[0])

    def compare_excel(self):
        df_old = pd.read_excel(self.label1.text())
        df_new = pd.read_excel(self.label2.text())

        print(df_old)

        # 불러온 데이터의 버전 구분
        df_old['ver'] = 'old'
        df_new['ver'] = 'new'

        # id_dropped = set(df_old[column_name]) - set(df_new[column_name])
        # id_added = set(df_new[column_name]) - set(df_old[column_name])
        #
        # # 삭제된 데이터
        # df_dropped = df_old[df_old[column_name].isin(id_dropped)].iloc[:, :-1]
        # # 추가된 데이터
        # df_added = df_new[df_new[column_name].isin(id_added)].iloc[:, :-1]
        #
        # df_concatted = pd.concat([df_old, df_new], ignore_index=True)
        # changes = df_concatted.drop_duplicates(df_concatted.columns[:-1], keep='last')
        # duplicated_list = changes[changes[column_name].duplicated()][column_name].to_list()
        # df_changed = changes[changes[column_name].isin(duplicated_list)]
        #
        # df_changed_old = df_changed[df_changed['ver'] == 'old'].iloc[:, :-1]
        # df_changed_old.sort_values(by=column_name, inplace=True)
        #
        # df_changed_new = df_changed[df_changed['ver'] == 'new'].iloc[:, :-1]
        # df_changed_new.sort_values(by=column_name, inplace=True)
        #
        # # 정보가 변경된 데이터 정리
        # df_info_changed = df_changed_old.copy()
        # for i in range(len(df_changed_new.index)):
        #     for j in range(len(df_changed_new.columns)):
        #         if (df_changed_new.iloc[i, j] != df_changed_old.iloc[i, j]):
        #             df_info_changed.iloc[i, j] = str(df_changed_old.iloc[i, j]) + " ==> " + str(df_changed_new.iloc[i, j])
        #
        # # 엑셀 저장
        # with pd.ExcelWriter('compared_result.xlsx') as writer:
        #     df_info_changed.to_excel(writer, sheet_name='info changed', index=False)
        #     df_added.to_excel(writer, sheet_name='added', index=False)
        #     df_dropped.to_excel(writer, sheet_name='dropped', index=False)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())