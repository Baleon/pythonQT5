import sys
from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication, QWidget, QMainWindow, QDoubleSpinBox, QComboBox


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        priceLabel = QLabel("{:>10}".format("Principal:"))
        rateLabel = QLabel("{:>10}".format("Rate:"))
        yearLabel = QLabel("{:>10}".format("Year:"))
        Amountlabel = QLabel("{:>10}".format("Amount:"))
        grid.addWidget(priceLabel, 0, 0)
        grid.addWidget(rateLabel, 1, 0)
        grid.addWidget(yearLabel, 2, 0)
        grid.addWidget(Amountlabel, 3, 0)

        self.pricelabelspinBox = QDoubleSpinBox()
        self.pricelabelspinBox.setRange(1, 1000000)
        self.pricelabelspinBox.setValue(1000)
        self.pricelabelspinBox.setPrefix("$ ")
        self.pricelabelspinBox.valueChanged.connect(self.updateUI)
        grid.addWidget(self.pricelabelspinBox, 0 ,1)

        self.ratelabelspinBox = QDoubleSpinBox()
        self.ratelabelspinBox.setRange(1, 100)
        self.ratelabelspinBox.setValue(5)
        self.ratelabelspinBox.setSuffix(" %")
        self.ratelabelspinBox.valueChanged.connect(self.updateUI)
        grid.addWidget(self.ratelabelspinBox, 1,1)

        self.yearCombox = QComboBox()
        self.yearCombox.addItems(("{} year".format(i) for i in range(1,11)))
        self.yearCombox.currentIndexChanged.connect(self.updateUI)
        grid.addWidget(self.yearCombox, 2, 1)

        self.amountlabel = QLabel("$")
        grid.addWidget(self.amountlabel, 3, 1)


        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('compound interest')

    def updateUI(self):
        """计算金额"""
        pricipal = self.pricelabelspinBox.value()
        rate = self.ratelabelspinBox.value()
        years = self.yearCombox.currentIndex() + 1
        ammount = pricipal * ((1 + rate / 100.0) ** years)
        self.amountlabel.setText("$ {:.2f}".format(ammount))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())