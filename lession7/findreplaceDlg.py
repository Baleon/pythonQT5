# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findreplaceDlg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FindAndReplaceDog(object):
    def setupUi(self, FindAndReplaceDog):
        FindAndReplaceDog.setObjectName("FindAndReplaceDog")
        FindAndReplaceDog.resize(400, 183)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(FindAndReplaceDog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(FindAndReplaceDog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.findlineEdit = QtWidgets.QLineEdit(FindAndReplaceDog)
        self.findlineEdit.setObjectName("findlineEdit")
        self.gridLayout.addWidget(self.findlineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(FindAndReplaceDog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replaceLineEdit = QtWidgets.QLineEdit(FindAndReplaceDog)
        self.replaceLineEdit.setObjectName("replaceLineEdit")
        self.gridLayout.addWidget(self.replaceLineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.caseCheckBox = QtWidgets.QCheckBox(FindAndReplaceDog)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtWidgets.QCheckBox(FindAndReplaceDog)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName("wholeCheckBox")
        self.horizontalLayout.addWidget(self.wholeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(FindAndReplaceDog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.syntaxCombox = QtWidgets.QComboBox(FindAndReplaceDog)
        self.syntaxCombox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.syntaxCombox.setObjectName("syntaxCombox")
        self.syntaxCombox.addItem("")
        self.horizontalLayout_2.addWidget(self.syntaxCombox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(FindAndReplaceDog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.findButton = QtWidgets.QPushButton(FindAndReplaceDog)
        self.findButton.setObjectName("findButton")
        self.verticalLayout_2.addWidget(self.findButton)
        self.replaceButton = QtWidgets.QPushButton(FindAndReplaceDog)
        self.replaceButton.setObjectName("replaceButton")
        self.verticalLayout_2.addWidget(self.replaceButton)
        self.replaceAllButton = QtWidgets.QPushButton(FindAndReplaceDog)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.verticalLayout_2.addWidget(self.replaceAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.closeButton = QtWidgets.QPushButton(FindAndReplaceDog)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.label.setBuddy(self.findlineEdit)
        self.label_2.setBuddy(self.replaceLineEdit)
        self.label_3.setBuddy(self.syntaxCombox)

        self.retranslateUi(FindAndReplaceDog)
        self.closeButton.clicked.connect(FindAndReplaceDog.reject)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDog)

    def retranslateUi(self, FindAndReplaceDog):
        _translate = QtCore.QCoreApplication.translate
        FindAndReplaceDog.setWindowTitle(_translate("FindAndReplaceDog", "Find and Replace"))
        self.label.setText(_translate("FindAndReplaceDog", "Find &What"))
        self.label_2.setText(_translate("FindAndReplaceDog", "Replace &with"))
        self.caseCheckBox.setText(_translate("FindAndReplaceDog", "&Case sensitive"))
        self.wholeCheckBox.setText(_translate("FindAndReplaceDog", "whole &words"))
        self.label_3.setText(_translate("FindAndReplaceDog", "&Syntax"))
        self.syntaxCombox.setItemText(0, _translate("FindAndReplaceDog", "Literal text"))
        self.findButton.setText(_translate("FindAndReplaceDog", "&Find"))
        self.replaceButton.setText(_translate("FindAndReplaceDog", "&Replace"))
        self.replaceAllButton.setText(_translate("FindAndReplaceDog", "Replace &All"))
        self.closeButton.setText(_translate("FindAndReplaceDog", "Close"))
