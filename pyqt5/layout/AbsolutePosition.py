import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication


class Example(QMainWindow):
    """
    we use move method to position our Qwiget, in our case these are labels,
    we position them by providing the x and y coordinates, the beginning of the
     coordinate system is at the left top corner
    """
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('code', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorial', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('absolute position')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())