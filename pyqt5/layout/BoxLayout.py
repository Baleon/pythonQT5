import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(okButton)
        hBox.addWidget(cancelButton)

        vBox = QVBoxLayout()
        vBox.addStretch(1)
        vBox.addLayout(hBox)

        self.setLayout(vBox)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Box layout")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())