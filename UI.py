# -*- coding: utf-8 -*-
import threading

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is run again.
# Do not edit this file unless you know what you are doing.
# Yujie Zhao, DYK team, St. Andrews, Scotland
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess, pyqtSignal, Qt, QObject
import main
import init
from threading import Thread

class helper(QObject):
    send_signal = pyqtSignal(str)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(722)
        MainWindow.setFixedHeight(569)
        MainWindow.setAutoFillBackground(True)
        QtWidgets.QApplication.processEvents()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        stylesheet = """
            #MainWindow{
            background-image: url(/home/UoPi/Pictures/JWST_2022-07-27_Jupiter-1024x971.png);
            background-repeat: no-repeat;
            background-position: center;}"""

        MainWindow.setStyleSheet(stylesheet)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 20, 661, 509))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setLineWidth(2)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.R_series_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.R_series_label.setObjectName("R_series_label")
        self.verticalLayout.addWidget(self.R_series_label)
        self.R_series_box = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.R_series_box.adjustSize()
        self.R_series_box.setEnabled(True)

        self.R_series_box.setTabletTracking(False)
        self.R_series_box.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.R_series_box.setAcceptDrops(False)
        self.R_series_box.setWhatsThis("")
        self.R_series_box.setAccessibleName("")
        self.R_series_box.setWrapping(False)
        self.R_series_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.R_series_box.setDecimals(1)
        self.R_series_box.setMaximum(100.0)
        self.R_series_box.setProperty("value", 1.5)
        self.R_series_box.setObjectName("R_series_box")
        self.verticalLayout.addWidget(self.R_series_box)
        self.R_shunt_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.R_shunt_label.setObjectName("R_shunt_label")
        self.verticalLayout.addWidget(self.R_shunt_label)
        self.R_shunt_box = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.R_shunt_box.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.R_shunt_box.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.R_shunt_box.setStatusTip("")
        self.R_shunt_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.R_shunt_box.setProperty("showGroupSeparator", False)
        self.R_shunt_box.setDecimals(1)
        self.R_shunt_box.setProperty("value", 25.0)
        self.R_shunt_box.setObjectName("R_shunt_box")
        self.verticalLayout.addWidget(self.R_shunt_box)
        self.C_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.C_label.setObjectName("C_label")
        self.verticalLayout.addWidget(self.C_label)
        self.C_box = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.C_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.C_box.setDecimals(2)
        self.C_box.setSingleStep(0.01)
        self.C_box.setProperty("value", 0.01)
        self.C_box.setObjectName("C_box")
        self.verticalLayout.addWidget(self.C_box)
        self.factor_up_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.factor_up_label.setObjectName("factor_up_label")
        self.verticalLayout.addWidget(self.factor_up_label)
        self.factor_up_box = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.factor_up_box.setMinimum(1)
        self.factor_up_box.setMaximum(20)
        self.factor_up_box.setProperty("value", 5)
        self.factor_up_box.setObjectName("factor_up_box")
        self.verticalLayout.addWidget(self.factor_up_box)
        self.factor_down_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.factor_down_label.setObjectName("factor_down_label")
        self.verticalLayout.addWidget(self.factor_down_label)
        self.factor_down_box = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.factor_down_box.setMinimum(1)
        self.factor_down_box.setMaximum(20)
        self.factor_down_box.setProperty("value", 5)
        self.factor_down_box.setObjectName("factor_down_box")
        self.verticalLayout.addWidget(self.factor_down_box)
        self.current_range_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.current_range_label.setObjectName("current_range_label")
        self.verticalLayout.addWidget(self.current_range_label)
        self.current_range_box = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.current_range_box.setMinimum(1)
        self.current_range_box.setMaximum(2)
        self.current_range_box.setObjectName("current_range_box")
        self.verticalLayout.addWidget(self.current_range_box)
        self.channel_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.channel_label.setObjectName("channel_label")
        self.verticalLayout.addWidget(self.channel_label)
        self.channel_box = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.channel_box.setMinimum(3)
        self.channel_box.setMaximum(6)
        self.channel_box.setObjectName("channel_box")
        self.verticalLayout.addWidget(self.channel_box)
        self.file_name_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.file_name_label.setObjectName("file_name_label")
        self.verticalLayout.addWidget(self.file_name_label)
        self.file_name_box = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.file_name_box.setObjectName("file_name_box")
        self.verticalLayout.addWidget(self.file_name_box)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.msg_browser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.msg_browser.setObjectName("msg_browser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.msg_browser)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 260)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thrust_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.thrust_label.setBaseSize(QtCore.QSize(0, 0))
        self.thrust_label.setObjectName("thrust_label")
        self.verticalLayout_2.addWidget(self.thrust_label)
        self.thrust_box = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.thrust_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.thrust_box.setMinimum(-1000.0)
        self.thrust_box.setMaximum(1000.0)
        self.thrust_box.setObjectName("thrust_box")
        self.verticalLayout_2.addWidget(self.thrust_box)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.run_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.run_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setObjectName("run_button")
        self.run_button.clicked.connect(self.run_func)
        self.verticalLayout_3.addWidget(self.run_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.R_series_label.setStyleSheet("QLabel#R_series_label {color: white;font-weight: bold;}")
        self.R_shunt_label.setStyleSheet("QLabel#R_shunt_label {color: white;font-weight: bold;}")
        self.C_label.setStyleSheet("QLabel#C_label {color: white;font-weight: bold;}")
        self.current_range_label.setStyleSheet("QLabel#current_range_label {color: white;font-weight: bold;}")
        self.factor_up_label.setStyleSheet("QLabel#factor_up_label {color: white;font-weight: bold;}")
        self.factor_down_label.setStyleSheet("QLabel#factor_down_label {color: white;font-weight: bold;}")
        self.channel_label.setStyleSheet("QLabel#channel_label {color: white;font-weight: bold;}")
        self.file_name_label.setStyleSheet("QLabel#file_name_label {color: white;font-weight: bold;}")
        self.thrust_label.setStyleSheet("QLabel#thrust_label {color: white;font-weight: bold;}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" color:333; font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Quantised Inertia Test Device</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GUI and program code by Yujie Zhao and Dmitriy Makhnovskiy</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DYK team</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">St. Andrews - Plymouth, UK, 10.09.2022</p></body></html>"))
        self.R_series_label.setText(_translate("MainWindow", "R_series (MOhms)"))
        self.R_shunt_label.setText(_translate("MainWindow", "R_shunt (MOhms)"))
        self.C_label.setText(_translate("MainWindow", "C (μF)"))
        self.factor_up_label.setText(_translate("MainWindow", "Factor up"))
        self.factor_down_label.setText(_translate("MainWindow", "Factor down"))
        self.current_range_label.setText(_translate("MainWindow", "Current range"))
        self.channel_label.setText(_translate("MainWindow", "Channel"))
        self.file_name_label.setText(_translate("MainWindow", "File name"))
        self.thrust_label.setText(_translate("MainWindow", "Thrust (mg)"))
        self.run_button.setText(_translate("MainWindow", "Run"))

    def run_func(self):
        r_series_ui = self.R_series_box.value()
        r_shunt_ui = self.R_shunt_box.value()
        c_ui = self.C_box.value()
        factor_up_ui = self.factor_up_box.value()
        factor_down_ui = self.factor_down_box.value()
        current_range_ui = self.current_range_box.value()
        channel_ui = self.channel_box.value()
        thrust_ui = self.thrust_box.value()
        name_ui = self.file_name_box.text()
        count = threading.active_count()
        print('Count of Thread: ',count)
        th = Thread(target=Ui_MainWindow.output,args=(self,r_series_ui, r_shunt_ui, c_ui, factor_up_ui, factor_down_ui, current_range_ui, channel_ui, thrust_ui,name_ui))
        th.start()
        count = threading.active_count()
        print('count of Thread after running main file: ',count)
        cur_count = threading.current_thread()
        print('current count for UI file: ', cur_count)

    def output(self,r_series_ui, r_shunt_ui, c_ui, factor_up_ui, factor_down_ui, current_range_ui, channel_ui, thrust_ui,name_ui):
        main.set_par(self,r_series_ui, r_shunt_ui, c_ui, factor_up_ui, factor_down_ui, current_range_ui, channel_ui, thrust_ui,name_ui)

    def printf(self,value):
        QtWidgets.QApplication.processEvents()
        self.msg_browser.append(value)
        verScrollBar = self.msg_browser.verticalScrollBar()
        verScrollBar.setValue(verScrollBar.maximum())

if __name__ == "__main__":
    import sys
    init.setting()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
