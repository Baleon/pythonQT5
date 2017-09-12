import sys
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):
    # 通过pyqtsignal创建内部类Commnunicate的一个属性，从而创建一个信号
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setWindowTitle('Emitting signals')


    def keyPressEvent(self, e: QtGui.QKeyEvent):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())