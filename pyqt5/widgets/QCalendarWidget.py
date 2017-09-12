
import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QCalendarWidget, QLabel


class Example(QWidget):
    """
    the example have a calendar and a label, the currently selected date is display in the label widget
    """
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('check box')

    def showDate(self, date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())