from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QSpinBox, QCheckBox, QDialogButtonBox, QGridLayout, QMessageBox


class NumberFormatDlg(QDialog):
    def __init__(self, format, parent = None):
        super(NumberFormatDlg, self).__init__(parent)

        thousandslabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandslabel.setBuddy(self.thousandsEdit)

        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)

        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        self.decimalPlacesSpinBox.setRange(0,6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.format = format.copy()

        grid = QGridLayout()
        grid.addWidget(thousandslabel, 0, 0)
        grid.addWidget(self.thousandsEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        grid.addWidget(self.redNegativesCheckBox,3, 0,1,2)
        grid.addWidget(btnBox,4, 0, 1, 2)
        self.setLayout(grid)

        btnBox.accepted.connect(self.accept)
        btnBox.rejected.connect(self.rejected)
        self.setWindowTitle("Set Number Format")

    def accept(self):
        class ThousandsError(Exception):pass
        class DecimalError(Exception):pass
        Punctuation = frozenset(" ,:;.")

        thousands = self.thousandsEdit.text()
        decimal = self.decimalMarkerEdit.text()
        try:
            if len(decimal) == 0:
                raise DecimalError("the decimal marker may not be empty")
            if len(thousands) > 1:
                raise  ThousandsError("the thousand separator may only be empty or one charactor")
            if len(decimal) > 1:
                raise  DecimalError("the decimal marker must be one charactor")
            if thousands == decimal:
                raise ThousandsError("the thousand and decimal must be different")
            if thousands and thousands not in Punctuation:
                raise ThousandsError("thousands must in Punctuation")
            if decimal not in Punctuation:
                raise DecimalError("decimal must in Punctuation")
        except ThousandsError as e:
            QMessageBox.warning(self, "thousand marker error", e)
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
            return
        except DecimalError as e:
            QMessageBox.warning(self, "decimal separator error", e)
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return

        self.format["thousandsseparator"] = thousands
        self.format["decimalmarker"] = decimal
        self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
        self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
        QDialog.accept(self)

    def numberFormat(self):
        return self.format




