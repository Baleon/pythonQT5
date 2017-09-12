import sys

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMessageBox
from qtpy import QtGui


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction('exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        exitAct.setStatusTip('Exiting Application')

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)


        self.setWindowTitle("MenuStatusTool Together")


    def closeEvent(self, a0: QtGui.QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'are you sure to quit', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            QCloseEvent.ignore()
        else:
            QCloseEvent.appect()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())