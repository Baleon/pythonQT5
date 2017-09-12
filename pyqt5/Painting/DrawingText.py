import random
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.text = "some one like you"

        self.setWindowTitle('check box')

    def paintEvent(self, e: QtGui.QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.drawText(e, qp)
        self.drawRect(qp)
        qp.end()

    def drawText(self, e:QtGui.QPaintEvent, qp):
        qp.setPen(QColor(168, 34,3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(e.rect(), Qt.AlignCenter, self.text)

        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() -1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x,y)

    def drawRect(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())