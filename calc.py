# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    firstPart = ""
    operator = ""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 446)
        self.dotBtn = QtWidgets.QPushButton(Dialog)
        self.dotBtn.setGeometry(QtCore.QRect(20, 370, 61, 51))
        self.dotBtn.setObjectName("dotBtn")
        self.zeroBtn = QtWidgets.QPushButton(Dialog)
        self.zeroBtn.setGeometry(QtCore.QRect(100, 370, 61, 51))
        self.zeroBtn.setObjectName("zeroBtn")
        self.equalBtn = QtWidgets.QPushButton(Dialog)
        self.equalBtn.setGeometry(QtCore.QRect(180, 370, 61, 51))
        self.equalBtn.setObjectName("equalBtn")
        self.multipleBtn = QtWidgets.QPushButton(Dialog)
        self.multipleBtn.setGeometry(QtCore.QRect(260, 370, 61, 51))
        self.multipleBtn.setObjectName("multipleBtn")
        self.divisionBtn = QtWidgets.QPushButton(Dialog)
        self.divisionBtn.setGeometry(QtCore.QRect(260, 300, 61, 51))
        self.divisionBtn.setObjectName("divisionBtn")
        self.eightBtn = QtWidgets.QPushButton(Dialog)
        self.eightBtn.setGeometry(QtCore.QRect(100, 300, 61, 51))
        self.eightBtn.setObjectName("eightBtn")
        self.nineBtn = QtWidgets.QPushButton(Dialog)
        self.nineBtn.setGeometry(QtCore.QRect(180, 300, 61, 51))
        self.nineBtn.setObjectName("nineBtn")
        self.sevenBtn = QtWidgets.QPushButton(Dialog)
        self.sevenBtn.setGeometry(QtCore.QRect(20, 300, 61, 51))
        self.sevenBtn.setObjectName("sevenBtn")
        self.fourBtn = QtWidgets.QPushButton(Dialog)
        self.fourBtn.setGeometry(QtCore.QRect(20, 230, 61, 51))
        self.fourBtn.setObjectName("fourBtn")
        self.sixBtn = QtWidgets.QPushButton(Dialog)
        self.sixBtn.setGeometry(QtCore.QRect(180, 230, 61, 51))
        self.sixBtn.setObjectName("sixBtn")
        self.minusBtn = QtWidgets.QPushButton(Dialog)
        self.minusBtn.setGeometry(QtCore.QRect(260, 230, 61, 51))
        self.minusBtn.setObjectName("minusBtn")
        self.fiveBtn = QtWidgets.QPushButton(Dialog)
        self.fiveBtn.setGeometry(QtCore.QRect(100, 230, 61, 51))
        self.fiveBtn.setObjectName("fiveBtn")
        self.twoBtn = QtWidgets.QPushButton(Dialog)
        self.twoBtn.setGeometry(QtCore.QRect(100, 160, 61, 51))
        self.twoBtn.setObjectName("twoBtn")
        self.oneBtn = QtWidgets.QPushButton(Dialog)
        self.oneBtn.setGeometry(QtCore.QRect(20, 160, 61, 51))
        self.oneBtn.setObjectName("oneBtn")
        self.threeBtn = QtWidgets.QPushButton(Dialog)
        self.threeBtn.setGeometry(QtCore.QRect(180, 160, 61, 51))
        self.threeBtn.setObjectName("threeBtn")
        self.plusBtn = QtWidgets.QPushButton(Dialog)
        self.plusBtn.setGeometry(QtCore.QRect(260, 160, 61, 51))
        self.plusBtn.setObjectName("plusBtn")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 34, 301, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.clearBtn = QtWidgets.QPushButton(Dialog)
        self.clearBtn.setGeometry(QtCore.QRect(20, 90, 61, 51))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Dialog)

        self.clearBtn.clicked.connect(self.lineEdit.clear)      # clear lineEdit
        self.clickBtn()                                         # other btn click

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dotBtn.setText(_translate("Dialog", "."))
        self.zeroBtn.setText(_translate("Dialog", "0"))
        self.equalBtn.setText(_translate("Dialog", "="))
        self.multipleBtn.setText(_translate("Dialog", "*"))
        self.divisionBtn.setText(_translate("Dialog", "/"))
        self.eightBtn.setText(_translate("Dialog", "8"))
        self.nineBtn.setText(_translate("Dialog", "9"))
        self.sevenBtn.setText(_translate("Dialog", "7"))
        self.fourBtn.setText(_translate("Dialog", "4"))
        self.sixBtn.setText(_translate("Dialog", "6"))
        self.minusBtn.setText(_translate("Dialog", "-"))
        self.fiveBtn.setText(_translate("Dialog", "5"))
        self.twoBtn.setText(_translate("Dialog", "2"))
        self.oneBtn.setText(_translate("Dialog", "1"))
        self.threeBtn.setText(_translate("Dialog", "3"))
        self.plusBtn.setText(_translate("Dialog", "+"))
        self.lineEdit.setText(_translate("Dialog", ""))
        self.clearBtn.setText(_translate("Dialog", "C"))

    def clickBtn(self):
        self.oneBtn.clicked.connect(self.setOneBtn)
        self.twoBtn.clicked.connect(self.setTwoBtn)
        self.threeBtn.clicked.connect(self.setThreeBtn)
        self.fourBtn.clicked.connect(self.setFourBtn)
        self.fiveBtn.clicked.connect(self.setFiveBtn)
        self.sixBtn.clicked.connect(self.setSixBtn)
        self.sevenBtn.clicked.connect(self.setSevenBtn)
        self.eightBtn.clicked.connect(self.setEightBtn)
        self.nineBtn.clicked.connect(self.setNineBtn)
        self.zeroBtn.clicked.connect(self.setZeroBtn)
        self.dotBtn.clicked.connect(self.setDotBtn)
        self.plusBtn.clicked.connect(self.setPlusBtn)
        self.minusBtn.clicked.connect(self.setMinusBtn)
        self.multipleBtn.clicked.connect(self.setMultipleBtn)
        self.divisionBtn.clicked.connect(self.setDivBtn)
        self.equalBtn.clicked.connect(self.setEqualBtn)


    def setPlusBtn(self):
        self.firstPart = self.lineEdit.text()
        self.operator = "+"
        self.lineEdit.setText("")


    def setMinusBtn(self):
        self.firstPart = self.lineEdit.text()
        self.operator = "-"
        self.lineEdit.setText("")


    def setMultipleBtn(self):
        self.firstPart = self.lineEdit.text()
        self.operator = "*"
        self.lineEdit.setText("")


    def setDivBtn(self):
        self.firstPart = self.lineEdit.text()
        self.operator = "/"
        self.lineEdit.setText("")


    def setEqualBtn(self):
        if self.operator == "+":
            self.lineEdit.setText(str(float(self.firstPart) + float(self.lineEdit.text())))

        elif self.operator == "-":
            self.lineEdit.setText(str(float(self.firstPart) - float(self.lineEdit.text())))

        elif self.operator == "/":
            self.lineEdit.setText(str(float(self.firstPart) / float(self.lineEdit.text())))

        elif self.operator == "*":
            self.lineEdit.setText(str(float(self.firstPart) * float(self.lineEdit.text())))


    def setOneBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.oneBtn.text())

    def setTwoBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.twoBtn.text())

    def setThreeBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.threeBtn.text())

    def setFourBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.fourBtn.text())

    def setFiveBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.fiveBtn.text())

    def setSixBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.sixBtn.text())

    def setSevenBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.sevenBtn.text())

    def setEightBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.eightBtn.text())

    def setNineBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.nineBtn.text())

    def setZeroBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.zeroBtn.text())

    def setDotBtn(self):
        self.lineEdit.setText(self.lineEdit.text() + self.dotBtn.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
