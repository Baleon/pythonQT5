import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')

        impMenu = QMenu("Import", self)
        impAct = QAction("Import mail", self)
        impMenu.addAction(impAct)

        newAct = QAction("new", self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Sub Menu')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())