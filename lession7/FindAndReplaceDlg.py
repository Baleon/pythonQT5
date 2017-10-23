import re

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication

from lession7.findreplaceDlg import Ui_FindAndReplaceDog


class FindAndReplaceDog(QDialog, Ui_FindAndReplaceDog):
    foundSignal = pyqtSignal(str,int)
    notFoundSignal = pyqtSignal(str)


    def __init__(self, text, parent=None):
        super(FindAndReplaceDog, self).__init__(parent=parent)

        self._text = text
        self._index = 0
        self.setupUi(self)

        self.findButton.clicked.connect(self.findButtonClicked)
        self.findlineEdit.textEdited.connect(self.findlineEditTxtEdit)
        self.replaceButton.clicked.connect(self.replaceButtonClick)
        self.replaceAllButton.clicked.connect(self.replaceAllButtonClick)
        self.updateUI()

    def updateUI(self):
        """
        根据findLineEdit控件是否有内容来判断findButton replaceButton replaceAllButton控件是否可用
        """
        # findLineEdit控件内容是否为空取反
        enable = not self.findlineEdit.text() == ""
        self.findButton.setEnabled(enable)
        self.replaceButton.setEnabled(enable)
        self.replaceAllButton.setEnabled(enable)

    def findButtonClicked(self):
        print("find button clicked")
        regex = self.makeReg()
        match = regex.search(self._text, self._index)
        if match is not None:
            self._index = match.end()
            self.foundSignal.emit("Found", match.start())

        else:
            self.notFoundSignal.emit("Not Found")

    def replaceButtonClick(self):
        regex = self.makeReg()
        self._text = regex.sub(self.replaceLineEdit.text(), self._text, 1)
        print(self._text)
    def findlineEditTxtEdit(self, text):
        self._index = 0
        # 更新控件可用性
        self.updateUI()
        print(text)

    def replaceAllButtonClick(self):
        regex = self.makeReg()
        self._text = regex.sub(self.replaceLineEdit.text(), self._text)

    def makeReg(self):
        findText = self.findlineEdit.text()
        if self.syntaxCombox.currentText() == "Literal text":
            re.escape(findText)

        flags = re.MULTILINE | re.DOTALL | re.UNICODE
        if not self.caseCheckBox.isChecked():
            flags |= re.IGNORECASE
        if self.wholeCheckBox.isChecked():
            findText = r"\b{0}\b".format(findText)

        return re.compile(findText, flags)

    def text(self):
        return self._text


if __name__ == '__main__':
    import sys

    text = """US experience shows that, unlike traditional patents,
    software patents do not encourage innovation and R&D, quite the
    contrary. In particular they hurt small and medium-sized enterprises
    and generally newcomers in the market. They will just weaken the market
    and increase spending on patents and litigation, at the expense of
    technological innovation and research. Especially dangerous are
    attempts to abuse the patent system by preventing interoperability as a
    means of avoiding competition with technological ability.
    --- Extract quoted from Linus Torvalds and Alan Cox's letter
    to the President of the European Parliament
    http://www.effi.org/patentit/patents_torvalds_cox.html"""


    def found(found, where):
        print(        "Found at %d" % where)

    def nomore():
        print(        "No more found")

    app = QApplication(sys.argv)
    form = FindAndReplaceDog(text)
    form.foundSignal.connect(found)
    form.notFoundSignal.connect(nomore)
    form.show()

    app.exec_()
