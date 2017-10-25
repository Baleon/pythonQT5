import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QAction, QApplication

from lession8.moviedata import *


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.movies = MovieContainer()

        self.table = QTableWidget()
        self.setCentralWidget(self.table)

        fileNewAction = QAction(self)
        fileNewAction.setText("&New")
        fileNewAction.set



        menuBar = self.menuBar()
        menu = menuBar.addMenu("&File")
        menu.addAction(fileNewAction)


    def createAction(self, text):
        action = QAction(text, self)

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())