import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Center Window')
        self.resize(250, 150)

        self.center()

    def center(self):
        qr = self.frameGeometry()
        # the QDesktopwidget class provides information about the user's desktop, including the screen size
    
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())