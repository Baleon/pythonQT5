import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QSlider, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        # here we have a valuechanged signal of the slider to the display of the lcd number
        # the sender is an object the sends a signal, the receiver is the object that receives the signal
        # the slot is the method that reacts the signal
        sld.valueChanged.connect(lcd.display)


        self.setWindowTitle('signal ans slot')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())