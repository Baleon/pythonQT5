import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QInputDialog


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('dialog', self)
        self.btn.clicked.connect(self.showdialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)


        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('input dialog')

    def showdialog(self):
        text, ok = QInputDialog.getText(self, 'input dialog', 'enter your name')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())