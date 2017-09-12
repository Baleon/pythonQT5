import sys
from PyQt5.QtCore import Qt, QMimeData
from PyQt5 import QtGui
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication


class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):
        if e.button() != Qt.LeftButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('button', self)
        self.button.move(100, 65)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('drag button')

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent):
        a0.accept()

    def dropEvent(self, e: QtGui.QDropEvent):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())