# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fitBackground.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FitBgDialog(object):
    def setupUi(self, FitBgDialog):
        if not FitBgDialog.objectName():
            FitBgDialog.setObjectName(u"FitBgDialog")
        FitBgDialog.resize(368, 665)
        self.verticalLayout_3 = QVBoxLayout(FitBgDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_6 = QWidget(FitBgDialog)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout = QVBoxLayout(self.widget_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_label = QLabel(self.widget_6)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(320, 320))
        self.result_label.setAutoFillBackground(True)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.widget_7 = QWidget(FitBgDialog)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_2 = QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.widget_7)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.source_label = QLabel(self.widget)
        self.source_label.setObjectName(u"source_label")

        self.horizontalLayout.addWidget(self.source_label)

        self.source_btn = QPushButton(self.widget)
        self.source_btn.setObjectName(u"source_btn")
        self.source_btn.setMinimumSize(QSize(81, 32))
        self.source_btn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout.addWidget(self.source_btn)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_7)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bg_label = QLabel(self.widget_2)
        self.bg_label.setObjectName(u"bg_label")

        self.horizontalLayout_2.addWidget(self.bg_label)

        self.bg_btn = QPushButton(self.widget_2)
        self.bg_btn.setObjectName(u"bg_btn")
        self.bg_btn.setMinimumSize(QSize(81, 32))
        self.bg_btn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout_2.addWidget(self.bg_btn)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_7)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.savepath_label = QLabel(self.widget_3)
        self.savepath_label.setObjectName(u"savepath_label")

        self.horizontalLayout_3.addWidget(self.savepath_label)

        self.savepath_btn = QPushButton(self.widget_3)
        self.savepath_btn.setObjectName(u"savepath_btn")
        self.savepath_btn.setMinimumSize(QSize(81, 32))
        self.savepath_btn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout_3.addWidget(self.savepath_btn)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_7)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.color_label = QLabel(self.widget_4)
        self.color_label.setObjectName(u"color_label")

        self.horizontalLayout_4.addWidget(self.color_label)

        self.colorRGBLabel = QLabel(self.widget_4)
        self.colorRGBLabel.setObjectName(u"colorRGBLabel")
        self.colorRGBLabel.setAutoFillBackground(True)
        self.colorRGBLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.colorRGBLabel)

        self.colorDialogBtn = QPushButton(self.widget_4)
        self.colorDialogBtn.setObjectName(u"colorDialogBtn")
        self.colorDialogBtn.setMinimumSize(QSize(81, 32))
        self.colorDialogBtn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout_4.addWidget(self.colorDialogBtn)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.fit_btn = QPushButton(self.widget_5)
        self.fit_btn.setObjectName(u"fit_btn")

        self.horizontalLayout_5.addWidget(self.fit_btn)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.widget_7)


        self.retranslateUi(FitBgDialog)

        QMetaObject.connectSlotsByName(FitBgDialog)
    # setupUi

    def retranslateUi(self, FitBgDialog):
        FitBgDialog.setWindowTitle(QCoreApplication.translate("FitBgDialog", u"Fit Background without changing ratio", None))
        self.result_label.setText(QCoreApplication.translate("FitBgDialog", u"Result", None))
        self.source_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Source Image Folder:", None))
        self.source_btn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.bg_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Background Image:", None))
        self.bg_btn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.savepath_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Results Saving Path:", None))
        self.savepath_btn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.color_label.setText(QCoreApplication.translate("FitBgDialog", u"BG Color:", None))
        self.colorRGBLabel.setText(QCoreApplication.translate("FitBgDialog", u"(255,255,255)", None))
        self.colorDialogBtn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.fit_btn.setText(QCoreApplication.translate("FitBgDialog", u"Fit!", None))
    # retranslateUi

