import sys
from PyQt5.QtWidgets import QDialog, QLabel, QSpinBox, QCheckBox, QComboBox, QPushButton, QWidget, QVBoxLayout, \
    QApplication, QHBoxLayout, QGridLayout, QDialogButtonBox
from PyQt5.QtCore import Qt


class PenPropertiesDlg(QDialog):
    """
    当一个对话框调用exec_()方法的时候，对话框的模态就会显示出来。只有在关闭这个对话框的情况下exec_的调用才会返回。
    """
    def __init__(self, parent = None):
        super(PenPropertiesDlg, self).__init__(parent=parent)
        widthlabel = QLabel('&Width:')
        self.widthspinbox = QSpinBox()
        widthlabel.setBuddy(self.widthspinbox)
        self.widthspinbox.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.widthspinbox.setRange(0, 24)

        self.beveledCheckBox = QCheckBox("&Beveled edges")
        # 在text中添加&的意义在于
        # 1. 字面上的与字符&
        # 2. 这个&不会显示出来，不过紧跟着其后的字符会以下划线开始
        stylelabel = QLabel('&Style')
        self.stylecombobox = QComboBox()
        stylelabel.setBuddy(self.stylecombobox)
        self.stylecombobox.addItems(('Solid', 'Dashed', 'Dotted', 'DashDotted', 'DashDotDotted'))

        # 针对于不同的
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch()
        buttonlayout.addWidget(buttonBox)

        gridlayout = QGridLayout()
        gridlayout.addWidget(widthlabel, 0, 0)
        gridlayout.addWidget(self.widthspinbox, 0 ,1)
        gridlayout.addWidget(self.beveledCheckBox, 0, 2)
        gridlayout.addWidget(stylelabel, 1, 0)
        gridlayout.addWidget(self.stylecombobox, 1, 1, 1, 2 )
        gridlayout.addLayout(buttonlayout, 2, 0, 1, 3)

        self.setLayout(gridlayout)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.width = 1
        self.beveled = False
        self.style = 'Solid'

        self.initUI()

    def initUI(self):
        penButtonInline = QPushButton('set button ....(Dumb &inline)')
        penButtonInline.clicked.connect(self.setPenInline)
        penButton = QPushButton('set pen...(Dumb &class)')
        penButton.clicked.connect(self.setPenProperties)
        self.label = QLabel('the pen has not benn set')
        self.label.setTextFormat(Qt.RichText)

        layout = QVBoxLayout()
        layout.addWidget(penButtonInline)
        layout.addWidget(penButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setWindowTitle("dialog")
        self.updateData()

    def setPenInline(self):
        widthlabel = QLabel('&Width:')
        self.widthspinbox = QSpinBox()
        widthlabel.setBuddy(self.widthspinbox)
        self.widthspinbox.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.widthspinbox.setRange(0, 24)

        self.beveledCheckBox = QCheckBox("&Beveled edges")
        # 在text中添加&的意义在于
        # 1. 字面上的与字符&
        # 2. 这个&不会显示出来，不过紧跟着其后的字符会以下划线开始
        stylelabel = QLabel('&Style')
        self.stylecombobox = QComboBox()
        stylelabel.setBuddy(self.stylecombobox)
        self.stylecombobox.addItems(('Solid', 'Dashed', 'Dotted', 'DashDotted', 'DashDotDotted'))

        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")

        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch()
        buttonlayout.addWidget(okButton)
        buttonlayout.addWidget(cancelButton)

        gridlayout = QGridLayout()
        gridlayout.addWidget(widthlabel, 0, 0)
        gridlayout.addWidget(self.widthspinbox, 0, 1)
        gridlayout.addWidget(self.beveledCheckBox, 0, 2)
        gridlayout.addWidget(stylelabel, 1, 0)
        gridlayout.addWidget(self.stylecombobox, 1, 1, 1, 2)
        gridlayout.addLayout(buttonlayout, 2, 0, 1, 3)

        form = QDialog()
        form.setLayout(gridlayout)
        okButton.clicked.connect(form.accept)
        cancelButton.clicked.connect(form.reject)
        if form.exec_():
            self.width = self.widthspinbox.value()
            self.beveled = self.beveledCheckBox.isChecked()
            self.style = self.stylecombobox.currentText()
            self.updateData()

    def setPenProperties(self):
        dialog = PenPropertiesDlg(self)
        dialog.widthspinbox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.stylecombobox.setCurrentIndex(
            dialog.stylecombobox.findText(self.style)
        )

        if dialog.exec_():
            self.width = dialog.widthspinbox.value()
            self.beveled = dialog.beveledCheckBox.isChecked()
            self.style = dialog.stylecombobox.currentText()
            self.updateData()

    def updateData(self):
        """在对话框显示完之后对对话框的选项进行显示"""
        bevel = ''
        if self.beveled:
            bevel = "<br>Beveled"
        self.label.setText("Width:{0}<br>Style={1}{2}".format(self.width, self.style, bevel))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())

