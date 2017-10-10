from PyQt5.QtCore import Qt, QRegExp, pyqtSignal
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QSpinBox, QCheckBox, QDialogButtonBox, QGridLayout, QMessageBox


class NumberFormatDlg(QDialog):
    _signal = pyqtSignal()

    def __init__(self, format, parent=None):
        super(NumberFormatDlg, self).__init__(parent)

        self.setAttribute(Qt.WA_DeleteOnClose)

        punctuationRe = QRegExp(r"[ ,;:.]")

        thousandslabel = QLabel("&Thousands separator")
        self.thousandEdit = QLineEdit(format["thousandsseparator"])
        thousandslabel.setBuddy(self.thousandEdit)
        self.thousandEdit.setMaxLength(1)
        self.thousandEdit.setValidator(QRegExpValidator(punctuationRe, self))

        decimalMaker = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMaker.setBuddy(self.decimalMarkerEdit)
        self.decimalMarkerEdit.setMaxLength(1)
        self.decimalMarkerEdit.setValidator(QRegExpValidator(punctuationRe, self))
        self.decimalMarkerEdit.setInputMask("X")

        decimalPlacesLabel = QLabel("&Decimal place")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Close)

        self.format = format

        grid = QGridLayout()
        grid.addWidget(thousandslabel, 0, 0)
        grid.addWidget(self.thousandEdit, 0, 1)
        grid.addWidget(decimalMaker, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        grid.addWidget(self.redNegativesCheckBox,3, 0,1,2)
        grid.addWidget(btnBox,4, 0, 1, 2)
        self.setLayout(grid)

        btnBox.accepted.connect(self.apply)
        btnBox.rejected.connect(self.reject)
        self.setWindowTitle("Set Number Format(Modeless)")

    def apply(self):
        thousands = self.thousandEdit.text()
        decimal = self.decimalMarkerEdit.text()

        if thousands == decimal:
            QMessageBox.warning(self, "format error", "the thousand and the decimal must be different")
            self.thousandEdit.selectAll()
            self.thousandEdit.setFocus()
            return

        if len(decimal) == 0:
            QMessageBox.warning(self, "format error", "the dicimal marker may not be empty")
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return

        self.format["thousandsseparator"] = thousands
        self.format["decimalmarker"] = decimal
        self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
        self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()


        self._signal.emit()



