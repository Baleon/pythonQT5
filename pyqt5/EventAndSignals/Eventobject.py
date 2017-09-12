import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.setLayout(grid)

        x,y = 0,0

        self.text = "x:{0},  y:{1}".format(x,y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0,0, Qt.AlignTop)


        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('event object')


    # Mouse tracking is disable be default, so the widget only receives the mouse move events when at least
    # one mouse button is pressed while the mouse is being moved, is mouse tacking is enable, the widget receives
    # mouse move events even if no buttons are press
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):

        x,y = e.x(),e.y()
        self.text = "x:{0},  y:{1}".format(x,y)
        self.label.setText(self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())