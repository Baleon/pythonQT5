
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # create a horizontal slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(30, 40, 100, 30)
        self.slider.setFocusPolicy(Qt.NoFocus)
        # connect the valuechanged signal to the user defined changeValue method
        self.slider.valueChanged[int].connect(self.changeValue)

        self.lab = QLabel(self)
        self.lab.move(50, 10)
        self.lab.setText('the score')


        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('check box')

    def changeValue(self, value):
        if value < 60:
            self.lab.setText("D")
        elif value >=60 and value < 80:
            self.lab.setText("C")
        elif value >= 80 and value <90:
            self.lab.setText('B')
        else:
            self.lab.setText("A")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())