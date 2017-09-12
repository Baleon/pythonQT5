import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, qApp, QApplication
from qtpy import QtGui


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Context Menu')
        self.setGeometry(300, 300, 300, 300)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent):
        cmenu = QMenu(self)
        newAct = cmenu.addAction('New')
        openAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())