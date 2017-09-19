"""
python QT GUI 快速编程
第四章：编程简介
第二课：简单计算器
"""
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, \
    QTextBrowser, QDialog, QLineEdit


class Example(QDialog):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.lineedit = QLineEdit()
        okButton = QPushButton('OK')
        hb = QHBoxLayout()
        hb.addStretch(1)
        hb.addWidget(self.lineedit)
        hb.addWidget(okButton)

        self.textbrowser = QTextBrowser()
        vb = QVBoxLayout()
        vb.addStretch(1)
        vb.addWidget(self.textbrowser)
        vb.addLayout(hb)
        self.setLayout(vb)

        okButton.clicked.connect(self.updateUI)

        self.setWindowTitle("Execute")
        self.setGeometry(300, 300, 300, 300)

    def updateUI(self):
        try:
            text = self.lineedit.text()
            self.textbrowser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.textbrowser.append("error!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())