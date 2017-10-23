from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

class NewImageDlg(QDialog):
    def __init__(self, parent=None):
        super(NewImageDlg, self).__init__(parent=parent)

        self.color = Qt.red