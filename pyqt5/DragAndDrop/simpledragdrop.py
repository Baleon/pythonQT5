import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLineEdit


class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        # enable drop events for the widget with setAcceptDrops
        self.setAcceptDrops(True)

    # reimplement the dragEnterEvent method, we inform about the data type that we accept
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('button', self)
        button.move(190, 65)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('drag and deop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())