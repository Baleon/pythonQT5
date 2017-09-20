"""
信号的使用
"""
import sys
from PyQt5.QtWidgets import QDialog, QDial, QSpinBox, QHBoxLayout, QApplication


class Example(QDialog):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.initUI()

    def initUI(self):
        dial = QDial()
        dial.setNotchesVisible(True)

        spinBox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinBox)
        self.setLayout(layout)
        # 无论是QDial还是QSpinBox都有valueChanged信号
        # 将这两个的信号和setValue之间进行连接，构成了相互影响的两个不减
        # 无论是哪个控件的值发生变化都会影响到另外一个部件。
        dial.valueChanged.connect(spinBox.setValue)
        spinBox.valueChanged.connect(dial.setValue)

        self.setWindowTitle("Signals and slots")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())