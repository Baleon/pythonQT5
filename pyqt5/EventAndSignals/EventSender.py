import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('EventHandler')

        vbox = QVBoxLayout()
        vbox.addStretch(2)


        btn = QPushButton('button 1', self)
        vbox.addWidget(btn)

        btn2 = QPushButton('button 2', self)
        vbox.addWidget(btn2)
        btn2.move(100, 0)

        self.setLayout(vbox)

        btn.clicked.connect(self.btnclick)
        btn2.clicked.connect(self.btnclick)

    def btnclick(self):
        sender = self.sender()
        self.statusbar.showMessage(sender.text() + "was pressed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())