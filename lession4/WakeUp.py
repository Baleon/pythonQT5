
"""
python QT GUI 快速编程
第四章：编程简介
第一课：25行弹出式闹钟
"""
import sys
import time
from PyQt5.QtCore import QTime, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

try:
    timeinput = input('input the alert time:HH:MM')
    due = QTime.currentTime()
    message = 'Alert'
    hours, mins = timeinput.split(':')
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
except ValueError:
    message = "Usage: alert you HH:MM"

while QTime.currentTime() < due:
    time.sleep(20)

# QLabel可以接受html文本
label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()

#设置单次定时器，python库中的time.sleep函数使用的是秒，而QTimer中使用的的是毫秒
#在singleshot中给定的两个参数的意义是在运行一分钟之后退出
#这种给定的方式叫做槽
QTimer.singleShot(60000, app.quit)
sys.exit(app.exec_())