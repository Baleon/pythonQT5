import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # similar to the menubar example above, we create an action object,
        # the object has a label and a shortcut, a quit method of the QtGui in connected to the triggered signal
        exitAct = QAction('exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tool Bar')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())