# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SingPage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.Background_label = QtWidgets.QLabel(self.centralwidget)
        self.Background_label.setGeometry(QtCore.QRect(0, 0, 320, 480))
        self.Background_label.setStyleSheet("background-image: url(:/background_image/wallpaper1.png);")
        self.Background_label.setText("")
        self.Background_label.setObjectName("Background_label")
        self.Dob = QtWidgets.QDateEdit(self.centralwidget)
        self.Dob.setGeometry(QtCore.QRect(150, 240, 141, 21))
        self.Dob.setAutoFillBackground(True)
        self.Dob.setProperty("showGroupSeparator", False)
        self.Dob.setCalendarPopup(True)
        self.Dob.setObjectName("Dob")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 240, 113, 21))
        self.lineEdit.setStyleSheet("font: 75 8pt \"MS Sans Serif\";\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255,0.5);\n"
"border:0;\n"
"color: rgb(85, 170, 255);\n"
"font-weight:bold;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 320, 50))
        self.label.setStyleSheet("background-color: rgb(60, 155, 230);\n"
"color: rgb(255, 255, 255);\n"
"font:italic 15pt \"MS Sans Serif\";\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255,0.5);\n"
"image: url(:/left_arrow/left_arrow.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.FirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstName.setGeometry(QtCore.QRect(30, 100, 121, 21))
        self.FirstName.setStyleSheet("font:  8pt \"MS Sans Serif\";\n"
"")
        self.FirstName.setObjectName("FirstName")
        self.LastName = QtWidgets.QLineEdit(self.centralwidget)
        self.LastName.setGeometry(QtCore.QRect(170, 100, 121, 21))
        self.LastName.setStyleSheet("font:  8pt \"MS Sans Serif\";\n"
"")
        self.LastName.setObjectName("LastName")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(30, 150, 261, 21))
        self.Email.setStyleSheet("font:  8pt \"MS Sans Serif\";\n"
"")
        self.Email.setObjectName("Email")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 190, 82, 21))
        self.radioButton.setStyleSheet("color: rgb(207, 207, 207);\n"
"font-weight:Bold;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 190, 82, 21))
        self.radioButton_2.setStyleSheet("color: rgb(207, 207, 207);\n"
"font-weight:Bold;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(220, 190, 82, 21))
        self.radioButton_3.setStyleSheet("color: rgb(207, 207, 207);\n"
"font-weight:Bold;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 300, 91, 23))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setTabletTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(60, 155, 230);\n"
"font: 10pt \"MS Sans Serif\";\n"
"font-weight:bold;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Date of Birth"))
        self.label.setText(_translate("MainWindow", "         Sign Up"))
        self.FirstName.setText(_translate("MainWindow", "First Name"))
        self.LastName.setText(_translate("MainWindow", "Last Name"))
        self.Email.setText(_translate("MainWindow", "Email Address"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.radioButton_3.setText(_translate("MainWindow", "Others"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))

import Background_rc
import back_arrow_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

