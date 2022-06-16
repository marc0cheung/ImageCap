# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomRotateUPfnaX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RandRotateDialog(object):
    def setupUi(self, RandRotateDialog):
        if not RandRotateDialog.objectName():
            RandRotateDialog.setObjectName(u"RandRotateDialog")
        RandRotateDialog.setEnabled(True)
        RandRotateDialog.resize(531, 650)
        self.source_label = QLabel(RandRotateDialog)
        self.source_label.setObjectName(u"source_label")
        self.source_label.setGeometry(QRect(20, 470, 381, 31))
        self.rotate_btn = QPushButton(RandRotateDialog)
        self.rotate_btn.setObjectName(u"rotate_btn")
        self.rotate_btn.setGeometry(QRect(210, 600, 131, 28))
        self.source_btn = QPushButton(RandRotateDialog)
        self.source_btn.setObjectName(u"source_btn")
        self.source_btn.setGeometry(QRect(420, 470, 93, 28))
        self.result_label = QLabel(RandRotateDialog)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(70, 20, 416, 416))
        self.result_label.setAutoFillBackground(True)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.savepath_btn = QPushButton(RandRotateDialog)
        self.savepath_btn.setObjectName(u"savepath_btn")
        self.savepath_btn.setGeometry(QRect(420, 510, 93, 28))
        self.savepath_label = QLabel(RandRotateDialog)
        self.savepath_label.setObjectName(u"savepath_label")
        self.savepath_label.setGeometry(QRect(20, 510, 381, 31))
        self.degree_input = QPlainTextEdit(RandRotateDialog)
        self.degree_input.setObjectName(u"degree_input")
        self.degree_input.setEnabled(False)
        self.degree_input.setGeometry(QRect(350, 550, 61, 31))
        self.degree_btn = QPushButton(RandRotateDialog)
        self.degree_btn.setObjectName(u"degree_btn")
        self.degree_btn.setEnabled(False)
        self.degree_btn.setGeometry(QRect(420, 550, 93, 28))
        self.degree_label = QLabel(RandRotateDialog)
        self.degree_label.setObjectName(u"degree_label")
        self.degree_label.setGeometry(QRect(20, 550, 201, 31))
        self.degree_checkbox = QCheckBox(RandRotateDialog)
        self.degree_checkbox.setObjectName(u"degree_checkbox")
        self.degree_checkbox.setGeometry(QRect(240, 548, 91, 31))
        self.degree_checkbox.setChecked(True)

        self.retranslateUi(RandRotateDialog)

        QMetaObject.connectSlotsByName(RandRotateDialog)
    # setupUi

    def retranslateUi(self, RandRotateDialog):
        RandRotateDialog.setWindowTitle(QCoreApplication.translate("RandRotateDialog", u"Random Rotate without losing full image", None))
        self.source_label.setText(QCoreApplication.translate("RandRotateDialog", u"Select Source Image Folder:", None))
        self.rotate_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Rotate!", None))
        self.source_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Select", None))
        self.result_label.setText(QCoreApplication.translate("RandRotateDialog", u"Result", None))
        self.savepath_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Select", None))
        self.savepath_label.setText(QCoreApplication.translate("RandRotateDialog", u"Select Results Saving Path:", None))
        self.degree_input.setPlainText(QCoreApplication.translate("RandRotateDialog", u"30", None))
        self.degree_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Save", None))
        self.degree_label.setText(QCoreApplication.translate("RandRotateDialog", u"Select Rotate Degree:", None))
        self.degree_checkbox.setText(QCoreApplication.translate("RandRotateDialog", u"Random?", None))
    # retranslateUi

