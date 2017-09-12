import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('MessageBox')


    # if wo close the widget the closeEvent is generated, to modify the widget behaviour we need to
    # reimplement the closeEvent() event handler
    def closeEvent(self, QCloseEvent):
        # show  a message box with tow buttons, yes and no, the first string appears on the titlebar, the
        # second string is the message text displayed by the dialog, the third argument specifies the combination
        # of buttons appearing in the dialog, the last parameter is the default button
        reply = QMessageBox.question(self, "Message", "are you sure to quit", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())