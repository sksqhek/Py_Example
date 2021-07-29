import sys
from sys import exit as sysExit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CentralPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent
        self.cbx = QComboBox()
        self.cbx.currentIndexChanged.connect(self.ChangeBDList)
        #self.cbx.setGeometry(700, 523, 930, 310)
        self.cbx123 = QComboBox()
        HBox = QHBoxLayout()
        HBox.addWidget(self.cbx)
        HBox.addWidget(QLabel('   '))
        HBox.addWidget(self.cbx123)
        HBox.addStretch(1)
        self.setLayout(HBox)
        #self.cbx123.setGeometry(930, 550, 1030, 310)
    def ChangeBDList(self, Index):
        self.Parent.UpdateBDList(Index)

        #window setGeometry (600, 450, 780, 280)
        #self.cbx.setGeometry (100, 73, 150, 30)
        #self.cbx123.setGeometry (330, 100, 250, 30)

class MyApp(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        super(MyApp,self).__init__()

        exitAction = QAction(QIcon('resources/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        moreAction = QAction(QIcon('resources/aboutus.png'), 'Our facebook page', self)
        moreAction.setShortcut('Ctrl+G')
        moreAction.setStatusTip('Facebook page link')

        self.statusBar().showMessage('Copyright 2020. Jersey Number Finder, all rights reserved.')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&Menu')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&More..')
        filemenu.addAction(moreAction)

        lbl = QLabel('<b>Player Name:</b>', self)
        lbl.setGeometry(QRect(30, 50, 110, 30))

        QToolTip.setFont(QFont('SansSerif', 10))
        lineE = QLineEdit('', self)
        lineE.setGeometry(QRect(150, 50, 430, 28))
        lineE.setToolTip('Enter your name or a nickname you want.')

        btn = QPushButton('Search By Name', self)
        btn.setGeometry(QRect(600, 50, 150, 30))
        btn.clicked.connect(QCoreApplication.instance().quit)

        cblbl = QLabel('<b>League:</b>', self)
        cblbl.setGeometry(QRect(30, 100, 70, 30))

        self.cb = {0:' 1. Bundesliga', 1: ' 2. Bundesliga', 2:' 3. Liga'}

        cblbl2 = QLabel('<b>Team:</b>', self)
        cblbl2.setGeometry(QRect(270, 100, 70, 30))

        self.cb1 = QComboBox(self)
        self.cb1.addItem(QIcon('resources/1.png'), ' 1. FC Union Berlin', self)
        self.cb1.addItem(QIcon('resources/2.png'), ' 1. FC Köln', self)
        self.cb1.addItem(QIcon('resources/3.png'), ' 1. FSV Mainz 05', self)
        self.cb1.addItem(QIcon('resources/4.png'), ' Bayer 04 Leverkusen', self)
        self.cb1.addItem(QIcon('resources/5.png'), ' Borussia Dortmund', self)
        self.cb1.addItem(QIcon('resources/6.png'), ' Borussia Mönchengladbach', self)
        self.cb1.addItem(QIcon('resources/7.png'), ' DSC Arminia Bielefeld', self)
        self.cb1.addItem(QIcon('resources/8.png'), ' Eintracht Frankfurt', self)
        self.cb1.addItem(QIcon('resources/9.png'), ' FC Augsburg', self)
        self.cb1.addItem(QIcon('resources/10.png'), ' FC Bayern München', self)
        self.cb1.addItem(QIcon('resources/11.png'), ' FC Schalke 04', self)
        self.cb1.addItem(QIcon('resources/12.png'), ' Hertha Berlin', self)
        self.cb1.addItem(QIcon('resources/13.png'), ' RB Leipzig', self)
        self.cb1.addItem(QIcon('resources/14.png'), ' Sport-Club Freiburg', self)
        self.cb1.addItem(QIcon('resources/15.png'), ' SV Werder Bremen', self)
        self.cb1.addItem(QIcon('resources/16.png'), ' TSG Hoffenheim', self)
        self.cb1.addItem(QIcon('resources/17.png'), ' VfB Stuttgart', self)
        self.cb1.addItem(QIcon('resources/18.png'), ' VfL Wolfsburg', self)

        self.cb2 = QComboBox(self)
        self.cb2.addItem(QIcon('resources/19.png'), ' 1. FC Heidenheim 1846', self)
        self.cb2.addItem(QIcon('resources/20.png'), ' 1. FC Nürnberg', self)
        self.cb2.addItem(QIcon('resources/21.png'), ' Eintracht Braunschweig', self)
        self.cb2.addItem(QIcon('resources/22.png'), ' FC Ergebirge Aue', self)
        self.cb2.addItem(QIcon('resources/23.png'), ' FC St. Pauli', self)
        self.cb2.addItem(QIcon('resources/24.png'), ' FC Würzburger Kicker', self)
        self.cb2.addItem(QIcon('resources/25.png'), ' Fortuna Düsseldorf', self)
        self.cb2.addItem(QIcon('resources/26.png'), ' Hamburger SV', self)
        self.cb2.addItem(QIcon('resources/27.png'), ' Hannover 96', self)
        self.cb2.addItem(QIcon('resources/28.png'), ' Holstein Kiel', self)
        self.cb2.addItem(QIcon('resources/29.png'), ' Karlsruher SC', self)
        self.cb2.addItem(QIcon('resources/30.png'), ' SC Paderborn 07', self)
        self.cb2.addItem(QIcon('resources/31.png'), ' SpVgg Greuther Fürth', self)
        self.cb2.addItem(QIcon('resources/32.png'), ' SSV Jahn Regensburg', self)
        self.cb2.addItem(QIcon('resources/33.png'), ' SV Darmstadt 98', self)
        self.cb2.addItem(QIcon('resources/34.png'), ' SV Sandhausen', self)
        self.cb2.addItem(QIcon('resources/35.png'), ' VfL Bochum 1848', self)
        self.cb2.addItem(QIcon('resources/36.png'), ' VfL Osnabrück', self)

        self.cb3 = QComboBox(self)
        self.cb3.addItem('')

        btn2 = QPushButton('Search By Team', self)
        btn2.setGeometry(QRect(600, 100, 150, 30))
        btn2.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("20/21 Deutsche League All-In-One Jersey Number Finder")
        self.setWindowIcon(QIcon('resources/icon.ico'))
        self.setGeometry(600, 450, 780, 280)
        self.show()

        self.CenterPane = CentralPanel(self)
        self.setCentralWidget(self.CenterPane)
        self.SetHome()

    def SetHome(self):
        self.CenterPane.cbx.clear()
        for key in self.cb.keys():
            self.CenterPane.cbx.insertItem(key, self.cb[key])

    def UpdateBDList(self, Index):
        ListUsed = []
        if Index == 0:
            ListUsed = self.cb1
        elif Index == 1:
            ListUsed = self.cb2
        elif  Index == 2:
            ListUsed = self.cb3
        self.CenterPane.cbx123.clear()
        if len(ListUsed) >= 0:
            Indx = 0
            for Item in ListUsed:
                self.CenterPane.cbx123.addItem(Item)
                Indx += 1

if __name__ == '__main__':
    import sys, time

    app = QApplication(sys.argv)

    splash_pix = QPixmap('resources/splashscreen.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    time.sleep(3)

    MainThred = QApplication([])
    MainGUI = MyApp()
    MainGUI.show()
    splash.finish(MainGUI)
    sysExit(MainThred.exec_())
