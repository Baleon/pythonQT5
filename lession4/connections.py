import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QHBoxLayout, QApplication, QLabel

class Example(QDialog):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hb = QHBoxLayout()
        for i in range(4):
            btn = QPushButton()
            btn.setText("Button {0}".format(i))
            # 针对每一个button把它的信号连接到同一个槽中
            btn.clicked.connect(self.buttonClicked)
            #btn.clicked.connect(lambda who:self.anyButton(btn.text()))
            hb.addWidget(btn)

        self.la = QLabel()
        self.la.setText("set window button click")
        hb.addWidget(self.la)

        self.setLayout(hb)
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('buttong connections')

    def buttonClicked(self):
        sender = self.sender()
        if sender is None or not isinstance(sender, QPushButton):
            return
        self.la.setText("{0} clicked".format(sender.text()))

    def anyButton(self, who):
        self.la.setText("{0} clikced".format(who))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())