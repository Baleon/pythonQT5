
import sys

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.probar = QProgressBar(self)
        self.probar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton(self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # to activate the progress bar we use the timer
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('check box')

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    def timerEvent(self, a0: 'QTimerEvent'):
        if self.step >=100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step += 1
        self.probar.setValue(self.step)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())