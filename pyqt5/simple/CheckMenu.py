import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Ready')

        menuBar = self.menuBar()
        viewMenu = menuBar.addMenu('view')

        viewAct = QAction('View statusbar', self, checkable=True)
        viewAct.setStatusTip('view statusbar')
        viewAct.setChecked(True)
        viewAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewAct)

        self.setGeometry(300, 300, 300,300)
        self.setWindowTitle('Check menu')

    def toggleMenu(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())