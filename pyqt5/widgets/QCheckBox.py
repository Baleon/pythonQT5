import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)


        self.setGeometry(300, 300, 300, 300)
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheck box')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())