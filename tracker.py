# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 421)
        icon = QtGui.QIcon.fromTheme("ico")
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: #373737;")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 120, 261, 251))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget{\n"
                                      "    background-color: #464646;\n"
                                      "    color:#ffc266;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 380, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 50, 31, 31))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ico/Audio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(26, 26))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 50, 31, 31))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Ico/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 50, 31, 31))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Ico/pluse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    color:#ffc266;\n"
                                   "}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(90, 50, 141, 31))
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "    background-color: rgb(124,113,116);\n"
                                       "    border-radius: 10px;\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk{\n"
                                       "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 115, 255), stop:1 rgba(255, 143, 64, 255));\n"
                                       "    border-radius: 10px;\n"
                                       "}")
        self.progressBar.setProperty("value", 20)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color: #464646;\n"
                                      "    color:#ffc266;\n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(100, 100, 100);\n"
                                      "}")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Ico/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 90, 81, 21))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Ico/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 90, 81, 21))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color: #464646;\n"
                                        "    color:#ffc266;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.pushButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Ico/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Audio player"))
        self.pushButton_4.setText(_translate("Form", "Add mp3"))
        self.pushButton_5.setText(_translate("Form", "Delete mp3"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
