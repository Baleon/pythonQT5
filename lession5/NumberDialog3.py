from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import *

"""
对话框没有任何按钮，在对话框中的每一个改动都会自动的应用到系统上。

在对话框关闭之后不是做销毁操作，而是对其进行隐藏。

如果需要设置关闭时候销毁窗口使用        
self.setAttribute(Qt.WA_DeleteOnClose)

"""
class NumberFormatDlg(QDialog):
    def __init__(self, format, callback, parent = None):
        super(NumberFormatDlg, self).__init__(parent=parent)

        punctuationRe = QRegExp(r"[ ,;:.]")
        thousandlabel = QLabel("&Thousands separator")
        self.thousandEdit = QLineEdit(format['thousandsseparator'])
        thousandlabel.setBuddy(self.thousandEdit)

        self.thousandEdit.setMaxLength(1)
        self.thousandEdit.setValidator(QRegExpValidator(punctuationRe,self))

        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format['decimalmarker'])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)

        self.decimalMarkerEdit.setMaxLength(1)
        self.decimalMarkerEdit.setValidator(QRegExpValidator(punctuationRe, self))
        # 遮挡符号
        self.decimalMarkerEdit.setInputMask('X')

        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        self.decimalPlacesSpinBox.setRange(0,6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        self.format = format
        self.callback = callback

        grid = QGridLayout()
        grid.addWidget(thousandlabel, 0, 0)
        grid.addWidget(self.thousandEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        grid.addWidget(self.redNegativesCheckBox,3, 0,1,2)
        self.setLayout(grid)

        self.thousandEdit.textEdited.connect(self.checkAndFix)
        self.decimalMarkerEdit.textEdited.connect(self.checkAndFix)
        self.decimalPlacesSpinBox.valueChanged.connect(self.apply)
        self.redNegativesCheckBox.toggled.connect(self.apply)
        self.setWindowTitle("Set Number Formate('live')")

    def checkAndFix(self):
        thousands = self.thousandEdit.text()
        decimal = self.decimalMarkerEdit.text()

        if thousands == decimal:
            self.thousandEdit.clear()
            self.thousandEdit.setFocus()

        if len(decimal) == 0:
            self.decimalMarkerEdit.setText(".")
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
        self.apply()

    def apply(self):
        self.format["thousandsseparator"] = self.thousandEdit.text()
        self.format["decimalmarker"] = self.decimalMarkerEdit.text()
        self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
        self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
        self.callback()




