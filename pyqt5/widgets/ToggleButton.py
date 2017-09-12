import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFrame


class Example(QWidget):
    """
    in this example create three toggle buttons and a QWidget, we set the background color of the QWidget to black
    the toggle button will toggle the red green and blue parts of the colour type, the background colour depends on
    which toggle buttons is pressed
    """
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # create the black background color
        self.cor = QColor(0,0,0)
        # to create a toggle button, we create a QPushButton and make it checkable by calling the setCheckable method
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10,60)
        # connect a clicked signal to our user defined method, we use the clicked signal that operates with a boolean value
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10,110)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10,160)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget {background-color:%s}' % self.cor.name())

        self.setGeometry(300, 300, 300,300)
        self.setWindowTitle('check box')

    def setColor(self, pressed):
        sender = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if sender.text() == "Red":
            self.cor.setRed(val)
        elif sender.text() == "Green":
            self.cor.setGreen(val)
        else:
            self.cor.setBlue(val)

        # use style sheets to change the background color the stylesheet is update with setStyleSheet() method
        self.square.setStyleSheet("QFrame {background-color:%s}" % self.cor.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())