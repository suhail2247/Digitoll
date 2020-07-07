# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FareDetails.ui'
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
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 320, 480))
        self.background.setStyleSheet("background-image: url(:/background_image/wallpaper1.png);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.top_bar = QtWidgets.QLabel(self.centralwidget)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 320, 50))
        self.top_bar.setStyleSheet("font: italic 15pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;\n"
"background-color: rgb(60, 155, 230);")
        self.top_bar.setObjectName("top_bar")
        self.back_arrow = QtWidgets.QLabel(self.centralwidget)
        self.back_arrow.setGeometry(QtCore.QRect(0, 0, 47, 51))
        self.back_arrow.setStyleSheet("image: url(:/left_arrow/left_arrow.png);")
        self.back_arrow.setText("")
        self.back_arrow.setObjectName("back_arrow")
        self.Total_Distance = QtWidgets.QLabel(self.centralwidget)
        self.Total_Distance.setGeometry(QtCore.QRect(20, 90, 131, 20))
        self.Total_Distance.setStyleSheet("color: rgb(60, 155, 230);\n"
"font: 11pt \"MS Sans Serif\";\n"
"font-weight:bold;")
        self.Total_Distance.setObjectName("Total_Distance")
        self.TotalTime = QtWidgets.QLabel(self.centralwidget)
        self.TotalTime.setGeometry(QtCore.QRect(20, 120, 141, 20))
        self.TotalTime.setStyleSheet("color: rgb(60, 155, 230);\n"
"font: 11pt \"MS Sans Serif\";\n"
"font-weight:bold;")
        self.TotalTime.setObjectName("TotalTime")
        self.Dist_value = QtWidgets.QLabel(self.centralwidget)
        self.Dist_value.setGeometry(QtCore.QRect(160, 90, 131, 20))
        self.Dist_value.setStyleSheet("color: rgb(207, 207, 207);\n"
"font: 11pt \"MS Sans Serif\";\n"
"font-weight:bold")
        self.Dist_value.setText("")
        self.Dist_value.setObjectName("Dist_value")
        self.Time_value = QtWidgets.QLabel(self.centralwidget)
        self.Time_value.setGeometry(QtCore.QRect(160, 120, 121, 16))
        self.Time_value.setStyleSheet("color: rgb(207, 207, 207);\n"
"font: 11pt \"MS Sans Serif\";\n"
"font-weight:bold")
        self.Time_value.setText("")
        self.Time_value.setObjectName("Time_value")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 150, 280, 1))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Tollplaze = QtWidgets.QLabel(self.centralwidget)
        self.Tollplaze.setGeometry(QtCore.QRect(30, 170, 101, 21))
        self.Tollplaze.setStyleSheet("color: rgb(60, 155, 230);\n"
"font:  italic 12pt \"MS Sans Serif\";\n"
"font-weight:bold;")
        self.Tollplaze.setObjectName("Tollplaze")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(186, 170, 61, 20))
        self.label.setStyleSheet("color: rgb(60, 155, 230);\n"
"font:  italic 12pt \"MS Sans Serif\";\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.ContinueBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ContinueBtn.setGeometry(QtCore.QRect(110, 400, 101, 31))
        self.ContinueBtn.setStyleSheet("background-color: rgb(60, 155, 230);\n"
"color: rgb(255, 255, 255);\n"
"font:10pt \"MS Sans Serif\";\n"
"font-weight:bold;")
        self.ContinueBtn.setObjectName("ContinueBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.top_bar.setText(_translate("MainWindow", "          Fare Details"))
        self.Total_Distance.setText(_translate("MainWindow", "Total Distance  "))
        self.TotalTime.setText(_translate("MainWindow", "Total  Time       "))
        self.Tollplaze.setText(_translate("MainWindow", "Toll Plazas"))
        self.label.setText(_translate("MainWindow", "Fare"))
        self.ContinueBtn.setText(_translate("MainWindow", "Continue"))

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

