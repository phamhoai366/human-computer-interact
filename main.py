from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import home, minesweeper, RPS, dino


ui = ''
app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_Dino.clicked.connect(dinoUi)
    ui.button_RPS_3.clicked.connect(rpsUi)
    ui.button_minesweeper.clicked.connect(minesweeperUi)
    MainWindow.show()

def rpsUi():
    global ui
    ui = RPS.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(homeUi)
    MainWindow.show()

def minesweeperUi():
    global ui
    ui = minesweeper.Ui_MainWindow()
    MainWindow.show()
      
def dinoUi():
    global ui
    ui = dino.App()
    ui.show()

#run app
homeUi()
sys.exit(app.exec())










