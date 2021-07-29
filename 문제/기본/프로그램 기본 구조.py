import sys
from sys import exit as sysExit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):

    def __init__(self):
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
        #btn.clicked.connect(QCoreApplication.instance().quit)

        cblbl = QLabel('<b>League:</b>', self)
        cblbl.setGeometry(QRect(30, 100, 70, 30))

        cb = QComboBox(self)
        cb.addItem(QIcon('resources/icon1.png'), ' 1. Bundesliga')
        cb.addItem(QIcon('resources/icon2.png'), ' 2. Bundesliga')
        cb.addItem(QIcon('resources/icon3.png'), ' 3. Liga')
        cb.setGeometry (100, 100, 150, 30)

        cblbl2 = QLabel('<b>Team:</b>', self)
        cblbl2.setGeometry(QRect(270, 100, 70, 30))

        cb1 = QComboBox(self)
        cb1.addItem(QIcon('resources/1.png'), ' 1. FC Union Berlin', self)
        cb1.addItem(QIcon('resources/2.png'), ' 1. FC Köln', self)
        cb1.addItem(QIcon('resources/3.png'), ' 1. FSV Mainz 05', self)
        cb1.addItem(QIcon('resources/4.png'), ' Bayer 04 Leverkusen', self)
        cb1.addItem(QIcon('resources/5.png'), ' Borussia Dortmund', self)
        cb1.addItem(QIcon('resources/6.png'), ' Borussia Mönchengladbach', self)
        cb1.addItem(QIcon('resources/7.png'), ' DSC Arminia Bielefeld', self)
        cb1.addItem(QIcon('resources/8.png'), ' Eintracht Frankfurt', self)
        cb1.addItem(QIcon('resources/9.png'), ' FC Augsburg', self)
        cb1.addItem(QIcon('resources/10.png'), ' FC Bayern München', self)
        cb1.addItem(QIcon('resources/11.png'), ' FC Schalke 04', self)
        cb1.addItem(QIcon('resources/12.png'), ' Hertha Berlin', self)
        cb1.addItem(QIcon('resources/13.png'), ' RB Leipzig', self)
        cb1.addItem(QIcon('resources/14.png'), ' Sport-Club Freiburg', self)
        cb1.addItem(QIcon('resources/15.png'), ' SV Werder Bremen', self)
        cb1.addItem(QIcon('resources/16.png'), ' TSG Hoffenheim', self)
        cb1.addItem(QIcon('resources/17.png'), ' VfB Stuttgart', self)
        cb1.addItem(QIcon('resources/18.png'), ' VfL Wolfsburg', self)
        cb1.move(330, 100)
        cb1.resize(250, 30)

        cb2 = QComboBox(self)
        cb2.addItem(QIcon('resources/19.png'), ' 1. FC Heidenheim 1846', self)
        cb2.addItem(QIcon('resources/20.png'), ' 1. FC Nürnberg', self)
        cb2.addItem(QIcon('resources/21.png'), ' Eintracht Braunschweig', self)
        cb2.addItem(QIcon('resources/22.png'), ' FC Ergebirge Aue', self)
        cb2.addItem(QIcon('resources/23.png'), ' FC St. Pauli', self)
        cb2.addItem(QIcon('resources/24.png'), ' FC Würzburger Kicker', self)
        cb2.addItem(QIcon('resources/25.png'), ' Fortuna Düsseldorf', self)
        cb2.addItem(QIcon('resources/26.png'), ' Hamburger SV', self)
        cb2.addItem(QIcon('resources/27.png'), ' Hannover 96', self)
        cb2.addItem(QIcon('resources/28.png'), ' Holstein Kiel', self)
        cb2.addItem(QIcon('resources/29.png'), ' Karlsruher SC', self)
        cb2.addItem(QIcon('resources/30.png'), ' SC Paderborn 07', self)
        cb2.addItem(QIcon('resources/31.png'), ' SpVgg Greuther Fürth', self)
        cb2.addItem(QIcon('resources/32.png'), ' SSV Jahn Regensburg', self)
        cb2.addItem(QIcon('resources/33.png'), ' SV Darmstadt 98', self)
        cb2.addItem(QIcon('resources/34.png'), ' SV Sandhausen', self)
        cb2.addItem(QIcon('resources/35.png'), ' VfL Bochum 1848', self)
        cb2.addItem(QIcon('resources/36.png'), ' VfL Osnabrück', self)
        cb2.move(330, 140)
        cb2.resize(250, 30)

        cb3 = QComboBox(self)
        cb3.addItem('')
        cb3.move(330, 180)
        cb3.resize(250,30)

        btn2 = QPushButton('Search By Team', self)
        btn2.setGeometry(QRect(600, 100, 150, 30))
        #btn2.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("20/21 Deutsche League All-In-One Jersey Number Finder")
        self.setWindowIcon(QIcon('resources/icon.ico'))
        self.setGeometry(600, 450, 780, 280)
        self.show()

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
