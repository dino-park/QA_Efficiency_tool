# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work1_viewer_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 597))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 3, 161, 161))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 12, 141, 141))
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/dino/Pictures/Netmarble_image/Netmarble_character_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 3, 621, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 100, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 14, 481, 141))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 371, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 241, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 361, 121))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(500)
        self.tableWidget.setColumnCount(19)
        self.tableWidget.setObjectName("tableWidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(390, 170, 391, 181))
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(0, 50, 381, 121))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 20, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 18, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 356, 501, 211))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(10, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(10, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_4.setFont(font)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(10, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_5.setFont(font)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_6.setFont(font)
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(10, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_7.setFont(font)
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        self.commandLinkButton_8 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_8.setGeometry(QtCore.QRect(140, 19, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_8.setFont(font)
        self.commandLinkButton_8.setObjectName("commandLinkButton_8")
        self.commandLinkButton_9 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_9.setGeometry(QtCore.QRect(140, 48, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_9.setFont(font)
        self.commandLinkButton_9.setObjectName("commandLinkButton_9")
        self.commandLinkButton_10 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_10.setGeometry(QtCore.QRect(140, 79, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_10.setFont(font)
        self.commandLinkButton_10.setObjectName("commandLinkButton_10")
        self.commandLinkButton_11 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_11.setGeometry(QtCore.QRect(140, 109, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_11.setFont(font)
        self.commandLinkButton_11.setObjectName("commandLinkButton_11")
        self.commandLinkButton_12 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_12.setGeometry(QtCore.QRect(140, 139, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_12.setFont(font)
        self.commandLinkButton_12.setObjectName("commandLinkButton_12")
        self.commandLinkButton_13 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_13.setGeometry(QtCore.QRect(140, 169, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_13.setFont(font)
        self.commandLinkButton_13.setObjectName("commandLinkButton_13")
        self.commandLinkButton_14 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_14.setGeometry(QtCore.QRect(300, 19, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_14.setFont(font)
        self.commandLinkButton_14.setObjectName("commandLinkButton_14")
        self.commandLinkButton_15 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_15.setGeometry(QtCore.QRect(300, 47, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_15.setFont(font)
        self.commandLinkButton_15.setObjectName("commandLinkButton_15")
        self.commandLinkButton_16 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_16.setGeometry(QtCore.QRect(300, 77, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_16.setFont(font)
        self.commandLinkButton_16.setObjectName("commandLinkButton_16")
        self.commandLinkButton_17 = QtWidgets.QCommandLinkButton(self.groupBox_5)
        self.commandLinkButton_17.setGeometry(QtCore.QRect(300, 108, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_17.setFont(font)
        self.commandLinkButton_17.setObjectName("commandLinkButton_17")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(520, 355, 261, 211))
        self.groupBox_6.setObjectName("groupBox_6")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(9, 15, 241, 191))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 157, 771, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 344, 771, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(376, 168, 20, 181))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(506, 354, 20, 211))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Welcome"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Apple System Status Check"))
        self.pushButton.setText(_translate("MainWindow", "Apple Srv."))
        self.pushButton_2.setText(_translate("MainWindow", "Developer Srv."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Crash Information"))
        self.pushButton_5.setText(_translate("MainWindow", "크래시율 조회(전일 기준, 2%이상 게임)"))
        self.tableWidget.setSortingEnabled(True)
        self.groupBox_4.setTitle(_translate("MainWindow", "Apple Product Information"))
        self.pushButton_6.setText(_translate("MainWindow", "로그인"))
        self.pushButton_7.setText(_translate("MainWindow", "조회"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Favorite"))
        self.pushButton_3.setText(_translate("MainWindow", "HostManager"))
        self.commandLinkButton.setText(_translate("MainWindow", "MConsole"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "CrashReport"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "BAS"))
        self.commandLinkButton_5.setText(_translate("MainWindow", "FMS"))
        self.commandLinkButton_6.setText(_translate("MainWindow", "JIRA"))
        self.commandLinkButton_7.setText(_translate("MainWindow", "Wiki"))
        self.commandLinkButton_8.setText(_translate("MainWindow", "GroupFi"))
        self.commandLinkButton_9.setText(_translate("MainWindow", "Mail"))
        self.commandLinkButton_10.setText(_translate("MainWindow", "Drive(Google)"))
        self.commandLinkButton_11.setText(_translate("MainWindow", "QA실 Drive"))
        self.commandLinkButton_12.setText(_translate("MainWindow", "넷마블개발자사이트"))
        self.commandLinkButton_13.setText(_translate("MainWindow", "GOB가이드(Wiki)"))
        self.commandLinkButton_14.setText(_translate("MainWindow", "Google Play Console"))
        self.commandLinkButton_15.setText(_translate("MainWindow", "Firebase Console"))
        self.commandLinkButton_16.setText(_translate("MainWindow", "Appstore Connect"))
        self.commandLinkButton_17.setText(_translate("MainWindow", "Apple Dev.Console"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
