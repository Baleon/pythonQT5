

# the QMainWindow class provides a main application window, this enables to create a classic application skeleton with
# a statubar, toolbar and a menubar
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # to get the status bar use the statusBar method
        self.statusBar().showMessage("Ready")


        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('menubar')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())