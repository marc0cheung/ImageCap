# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fitBackgroundQzCLXH.ui'
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
        FitBgDialog.resize(555, 685)
        self.result_label = QLabel(FitBgDialog)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(80, 20, 416, 416))
        self.result_label.setAutoFillBackground(True)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.bg_label = QLabel(FitBgDialog)
        self.bg_label.setObjectName(u"bg_label")
        self.bg_label.setGeometry(QRect(30, 510, 381, 31))
        self.source_label = QLabel(FitBgDialog)
        self.source_label.setObjectName(u"source_label")
        self.source_label.setGeometry(QRect(30, 470, 381, 31))
        self.source_btn = QPushButton(FitBgDialog)
        self.source_btn.setObjectName(u"source_btn")
        self.source_btn.setGeometry(QRect(430, 470, 93, 28))
        self.bg_btn = QPushButton(FitBgDialog)
        self.bg_btn.setObjectName(u"bg_btn")
        self.bg_btn.setGeometry(QRect(430, 510, 93, 28))
        self.fit_btn = QPushButton(FitBgDialog)
        self.fit_btn.setObjectName(u"fit_btn")
        self.fit_btn.setGeometry(QRect(220, 640, 131, 28))
        self.color_input = QPlainTextEdit(FitBgDialog)
        self.color_input.setObjectName(u"color_input")
        self.color_input.setGeometry(QRect(270, 590, 151, 31))
        self.color_btn = QPushButton(FitBgDialog)
        self.color_btn.setObjectName(u"color_btn")
        self.color_btn.setGeometry(QRect(430, 590, 93, 28))
        self.color_label = QLabel(FitBgDialog)
        self.color_label.setObjectName(u"color_label")
        self.color_label.setGeometry(QRect(30, 590, 201, 31))
        self.savepath_btn = QPushButton(FitBgDialog)
        self.savepath_btn.setObjectName(u"savepath_btn")
        self.savepath_btn.setGeometry(QRect(430, 550, 93, 28))
        self.savepath_label = QLabel(FitBgDialog)
        self.savepath_label.setObjectName(u"savepath_label")
        self.savepath_label.setGeometry(QRect(30, 550, 381, 31))

        self.retranslateUi(FitBgDialog)

        QMetaObject.connectSlotsByName(FitBgDialog)
    # setupUi

    def retranslateUi(self, FitBgDialog):
        FitBgDialog.setWindowTitle(QCoreApplication.translate("FitBgDialog", u"Fit Background without changing ratio", None))
        self.result_label.setText(QCoreApplication.translate("FitBgDialog", u"Result", None))
        self.bg_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Background Image:", None))
        self.source_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Source Image Folder:", None))
        self.source_btn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.bg_btn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.fit_btn.setText(QCoreApplication.translate("FitBgDialog", u"Fit!", None))
        self.color_input.setPlainText(QCoreApplication.translate("FitBgDialog", u"N/A Currently", None))
        self.color_btn.setText(QCoreApplication.translate("FitBgDialog", u"Save", None))
        self.color_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Background Color:", None))
        self.savepath_btn.setText(QCoreApplication.translate("FitBgDialog", u"Select", None))
        self.savepath_label.setText(QCoreApplication.translate("FitBgDialog", u"Select Results Saving Path:", None))
    # retranslateUi

