import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QTextEdit


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(author,2,0)
        grid.addWidget(review, 3, 0)

        grid.addWidget(titleEdit, 1,1)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setWindowTitle('Review')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =Example()
    ex.show()
    sys.exit(app.exec_())