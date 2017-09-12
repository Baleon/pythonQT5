

"""
信号和槽，在之后的学习会了解这两个qt的核心东西
"""
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('quit', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # 信号和槽的使用
        # 当我们按下这个按钮的时候，释放了click这个信号，槽可以是QT或者python
        btn.clicked.connect(QCoreApplication.quit)

        self.setGeometry(200, 300, 400, 500)
        self.setWindowTitle("QUIT")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())