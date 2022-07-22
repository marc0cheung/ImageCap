# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imagecap_panel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(581, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VideoStream_Widget = QWidget(self.centralwidget)
        self.VideoStream_Widget.setObjectName(u"VideoStream_Widget")
        self.horizontalLayout_4 = QHBoxLayout(self.VideoStream_Widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.videoStream = QLabel(self.VideoStream_Widget)
        self.videoStream.setObjectName(u"videoStream")
        self.videoStream.setMinimumSize(QSize(416, 416))
        self.videoStream.setMaximumSize(QSize(416, 416))
        self.videoStream.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.videoStream)

        self.horizontalSpacer_9 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addWidget(self.VideoStream_Widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.PrefSet_Widget = QWidget(self.centralwidget)
        self.PrefSet_Widget.setObjectName(u"PrefSet_Widget")
        self.PrefSet_Widget.setMinimumSize(QSize(557, 73))
        self.horizontalLayout_3 = QHBoxLayout(self.PrefSet_Widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.WidthSet_Widget = QWidget(self.PrefSet_Widget)
        self.WidthSet_Widget.setObjectName(u"WidthSet_Widget")
        self.WidthSet_Widget.setMinimumSize(QSize(98, 62))
        self.verticalLayout_2 = QVBoxLayout(self.WidthSet_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.width_label = QLabel(self.WidthSet_Widget)
        self.width_label.setObjectName(u"width_label")
        font = QFont()
        font.setPointSize(12)
        self.width_label.setFont(font)

        self.verticalLayout_2.addWidget(self.width_label)

        self.width_input = QLineEdit(self.WidthSet_Widget)
        self.width_input.setObjectName(u"width_input")
        self.width_input.setMinimumSize(QSize(36, 21))
        self.width_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.width_input)


        self.horizontalLayout_3.addWidget(self.WidthSet_Widget)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.HeightSet_Widget = QWidget(self.PrefSet_Widget)
        self.HeightSet_Widget.setObjectName(u"HeightSet_Widget")
        self.HeightSet_Widget.setMinimumSize(QSize(97, 62))
        self.verticalLayout_3 = QVBoxLayout(self.HeightSet_Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.height_label = QLabel(self.HeightSet_Widget)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setFont(font)

        self.verticalLayout_3.addWidget(self.height_label)

        self.height_input = QLineEdit(self.HeightSet_Widget)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setMinimumSize(QSize(35, 21))
        self.height_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.height_input)


        self.horizontalLayout_3.addWidget(self.HeightSet_Widget)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.IndexSet_Widget = QWidget(self.PrefSet_Widget)
        self.IndexSet_Widget.setObjectName(u"IndexSet_Widget")
        self.IndexSet_Widget.setMinimumSize(QSize(98, 62))
        self.verticalLayout_4 = QVBoxLayout(self.IndexSet_Widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.index_label = QLabel(self.IndexSet_Widget)
        self.index_label.setObjectName(u"index_label")
        self.index_label.setFont(font)

        self.verticalLayout_4.addWidget(self.index_label)

        self.index_input = QLineEdit(self.IndexSet_Widget)
        self.index_input.setObjectName(u"index_input")
        self.index_input.setMinimumSize(QSize(36, 21))
        self.index_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.index_input)


        self.horizontalLayout_3.addWidget(self.IndexSet_Widget)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.SaveIndexBtn = QPushButton(self.PrefSet_Widget)
        self.SaveIndexBtn.setObjectName(u"SaveIndexBtn")

        self.horizontalLayout_3.addWidget(self.SaveIndexBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.PrefSet_Widget)

        self.FuncBtn_Widget = QWidget(self.centralwidget)
        self.FuncBtn_Widget.setObjectName(u"FuncBtn_Widget")
        self.FuncBtn_Widget.setMinimumSize(QSize(0, 51))
        self.horizontalLayout = QHBoxLayout(self.FuncBtn_Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.FitBgBtn = QPushButton(self.FuncBtn_Widget)
        self.FitBgBtn.setObjectName(u"FitBgBtn")

        self.horizontalLayout.addWidget(self.FitBgBtn)

        self.RandRotateBtn = QPushButton(self.FuncBtn_Widget)
        self.RandRotateBtn.setObjectName(u"RandRotateBtn")

        self.horizontalLayout.addWidget(self.RandRotateBtn)

        self.RotateBtn = QPushButton(self.FuncBtn_Widget)
        self.RotateBtn.setObjectName(u"RotateBtn")

        self.horizontalLayout.addWidget(self.RotateBtn)

        self.CapBtn = QPushButton(self.FuncBtn_Widget)
        self.CapBtn.setObjectName(u"CapBtn")

        self.horizontalLayout.addWidget(self.CapBtn)

        self.CloseBtn = QPushButton(self.FuncBtn_Widget)
        self.CloseBtn.setObjectName(u"CloseBtn")

        self.horizontalLayout.addWidget(self.CloseBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.FuncBtn_Widget)

        self.SavePath_Widget = QWidget(self.centralwidget)
        self.SavePath_Widget.setObjectName(u"SavePath_Widget")
        self.SavePath_Widget.setMinimumSize(QSize(0, 44))
        self.horizontalLayout_2 = QHBoxLayout(self.SavePath_Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.path_label = QLabel(self.SavePath_Widget)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.path_label)

        self.SelcPathBtn = QPushButton(self.SavePath_Widget)
        self.SelcPathBtn.setObjectName(u"SelcPathBtn")
        self.SelcPathBtn.setMinimumSize(QSize(81, 32))
        self.SelcPathBtn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout_2.addWidget(self.SelcPathBtn)


        self.verticalLayout.addWidget(self.SavePath_Widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ImageCap V1.2", None))
        self.videoStream.setText(QCoreApplication.translate("MainWindow", u"Video Stream", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.width_input.setText(QCoreApplication.translate("MainWindow", u"416", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.height_input.setText(QCoreApplication.translate("MainWindow", u"416", None))
        self.index_label.setText(QCoreApplication.translate("MainWindow", u"Index:", None))
        self.index_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SaveIndexBtn.setText(QCoreApplication.translate("MainWindow", u"Save Pref.", None))
        self.FitBgBtn.setText(QCoreApplication.translate("MainWindow", u"Fit BG", None))
        self.RandRotateBtn.setText(QCoreApplication.translate("MainWindow", u"ImageRotate", None))
        self.RotateBtn.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.CapBtn.setText(QCoreApplication.translate("MainWindow", u"Cap!", None))
        self.CloseBtn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"Select Capture Path...", None))
        self.SelcPathBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
    # retranslateUi

