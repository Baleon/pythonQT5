import sys
from PyQt5.QtWidgets import QDialog, QListWidget, QVBoxLayout, QPushButton, QApplication, QHBoxLayout, QInputDialog, \
    QLineEdit, QMessageBox




class StringListDlg(QDialog):
    def __init__(self, name, stringList = None, parent = None):
        super(StringListDlg, self).__init__(parent=parent)

        self.name = name
        self.listWidget = QListWidget()
        if stringList is not None:
            self.listWidget.addItems(stringList)
            self.listWidget.setCurrentRow(0)

        buttonlayout = QVBoxLayout()
        for text, slot in (("&Add...", self.add),
                           ("&Edit...", self.edit),
                           ("&Remove.", self.remove),
                           ("&Up....", self.up),
                           ("&Down...", self.down),
                           ("&Sort...", self.listWidget.sortItems),
                           ("&Close...", self.accept)):
            button = QPushButton(text)

            buttonlayout.addWidget(button)
            button.clicked.connect(slot)


        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(buttonlayout)
        self.setLayout(layout)
        self.setWindowTitle("Edit %s List" % self.name)


    def add(self):
        row = self.listWidget.currentRow()
        title = "Add %s" % self.name
        string, ok = QInputDialog.getText(self, title, title)
        if ok and string:
            self.listWidget.insertItem(row, string)

    def edit(self):
        item = self.listWidget.currentItem()
        if item is not None:
            title = "Edit %s" % self.name
            string, ok = QInputDialog.getText(self, title, title, QLineEdit.Normal, item.text())

            if ok and string:
                item.setText(string)

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.currentItem()
        if item is not None:
            reply = QMessageBox.question(self, "remove %s" % self.name,"remove {0} {1}".format(self.name, item.text()),
                                         QMessageBox.Ok | QMessageBox.No)
            if reply == QMessageBox.Ok:
                item = self.listWidget.takeItem(row)
                del item

    def up(self):
        row = self.listWidget.currentRow()
        if row >= 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1 ,item)
            self.listWidget.setCurrentRow(row - 1)

    def down(self):
        row = self.listWidget.currentRow()
        if row <= self.listWidget.count():
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1 ,item)
            self.listWidget.setCurrentRow(row + 1)

    def accept(self):
        pass


if __name__ == '__main__':
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
             "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
             "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry",
             "Orange"]
    app = QApplication(sys.argv)
    form = StringListDlg("Fruit", fruit)
    form.exec_()
    print("\n".join([x for x in form.stringlist]))