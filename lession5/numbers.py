import random
import string
import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout

from lession5 import NumberDialog1
from lession5 import NumberDialog2
from lession5 import NumberDialog3


class Example(QWidget):
    X_MAX = 26
    Y_MAX = 60

    def __init__(self):
        super(Example, self).__init__()
        self.format = dict(thousandsseparator=",", decimalmarker = ".", decimalplaces = 2, rednegatives =False)

        self.numberFormatDlg = None

        # 随机生成数据
        self.numbers = {}
        for i in range(self.X_MAX):
            for j in range(self.Y_MAX):
                self.numbers[(i, j)] = (10000 * random.random()) - 5000

        self.initUI()
        # 刷新数据显示
        self.refreshTable()


    def initUI(self):
        self.table = QTableWidget()

        hlayout = QHBoxLayout()
        hlayout.addStretch()
        formatbutton1 = QPushButton("set number Format(&Modal)")
        formatbutton1.clicked.connect(self.formatbuttonclicked)
        hlayout.addWidget(formatbutton1)

        formatbutton2 = QPushButton("Set number Format(Modele&ss)")
        formatbutton2.clicked.connect(self.formatbutton2clicked)
        hlayout.addWidget(formatbutton2)

        formatbutton3 = QPushButton("Set number Format((`&Live'))")
        formatbutton3.clicked.connect(self.formatbutton3clicked)
        hlayout.addWidget(formatbutton3)


        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(hlayout)

        self.setLayout(layout)

        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('number')

    def formatbuttonclicked(self):
        dialog = NumberDialog1.NumberFormatDlg(self.format, self)
        if dialog.exec_():
            self.format = dialog.numberFormat()
            self.refreshTable()

    def formatbutton2clicked(self):
        try:
            dialog = NumberDialog2.NumberFormatDlg(self.format, self)
        except Exception as e:
            print(e)
        dialog._signal.connect(self.refreshTable)
        dialog.show()

    def formatbutton3clicked(self):
        if self.numberFormatDlg is None:
            self.numberFormatDlg = NumberDialog3.NumberFormatDlg(self.format, self.refreshTable, self)

        self.numberFormatDlg.show()
        # 将对话框提升，放到所有窗口的上方
        self.numberFormatDlg.raise_()
        # 激活对话框
        self.numberFormatDlg.activateWindow()


    def refreshTable(self):
        self.table.clear()
        self.table.setColumnCount(self.X_MAX)
        self.table.setRowCount(self.Y_MAX)
        self.table.setHorizontalHeaderLabels(list(string.ascii_uppercase))
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                fraction, whole = math.modf(self.numbers[(x, y)])
                sign = "-" if whole < 0 else ""
                whole = "{0}".format(math.floor(abs(whole)))
                digits = []
                # 按照规定的方式每三位在之间添加一个符号
                for i, digit in enumerate(reversed(whole)):
                    if i and i % 3 == 0:
                        digits.insert(0, self.format["thousandsseparator"])
                    digits.insert(0, digit)

                if self.format["decimalmarker"]:
                    fraction = "{:0.7f}".format(abs(fraction))
                    fraction = (self.format["decimalmarker"] + fraction[2:self.format["decimalplaces"] + 2])
                else:
                    fraction = ""

                showtext = "{0}{1}{2}".format(sign,"".join(digits), fraction)
                item = QTableWidgetItem(showtext)
                item.setTextAlignment(Qt.AlignRight|Qt.AlignCenter)
                if sign and self.format["rednegatives"]:
                    item.setBackground(Qt.red)
                self.table.setItem(y, x, item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())