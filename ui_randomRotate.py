# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomRotate.ui'
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
        RandRotateDialog.resize(397, 612)
        self.verticalLayout_3 = QVBoxLayout(RandRotateDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Result_Widget = QWidget(RandRotateDialog)
        self.Result_Widget.setObjectName(u"Result_Widget")
        self.verticalLayout = QVBoxLayout(self.Result_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_label = QLabel(self.Result_Widget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(320, 320))
        self.result_label.setAutoFillBackground(True)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)


        self.verticalLayout_3.addWidget(self.Result_Widget)

        self.Control_Widget = QWidget(RandRotateDialog)
        self.Control_Widget.setObjectName(u"Control_Widget")
        self.Control_Widget.setMaximumSize(QSize(16777215, 234))
        self.verticalLayout_2 = QVBoxLayout(self.Control_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SourceSelect_Widget = QWidget(self.Control_Widget)
        self.SourceSelect_Widget.setObjectName(u"SourceSelect_Widget")
        self.SourceSelect_Widget.setMaximumSize(QSize(16777215, 44))
        self.horizontalLayout = QHBoxLayout(self.SourceSelect_Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.source_label = QLabel(self.SourceSelect_Widget)
        self.source_label.setObjectName(u"source_label")

        self.horizontalLayout.addWidget(self.source_label)

        self.source_btn = QPushButton(self.SourceSelect_Widget)
        self.source_btn.setObjectName(u"source_btn")
        self.source_btn.setMinimumSize(QSize(81, 32))
        self.source_btn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout.addWidget(self.source_btn)


        self.verticalLayout_2.addWidget(self.SourceSelect_Widget)

        self.SavePathSelect_Widget = QWidget(self.Control_Widget)
        self.SavePathSelect_Widget.setObjectName(u"SavePathSelect_Widget")
        self.SavePathSelect_Widget.setMaximumSize(QSize(16777215, 44))
        self.horizontalLayout_2 = QHBoxLayout(self.SavePathSelect_Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.savepath_label = QLabel(self.SavePathSelect_Widget)
        self.savepath_label.setObjectName(u"savepath_label")

        self.horizontalLayout_2.addWidget(self.savepath_label)

        self.savepath_btn = QPushButton(self.SavePathSelect_Widget)
        self.savepath_btn.setObjectName(u"savepath_btn")
        self.savepath_btn.setMinimumSize(QSize(81, 32))
        self.savepath_btn.setMaximumSize(QSize(81, 32))

        self.horizontalLayout_2.addWidget(self.savepath_btn)


        self.verticalLayout_2.addWidget(self.SavePathSelect_Widget)

        self.RotateDegree_Widget = QWidget(self.Control_Widget)
        self.RotateDegree_Widget.setObjectName(u"RotateDegree_Widget")
        self.RotateDegree_Widget.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.RotateDegree_Widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.degree_label = QLabel(self.RotateDegree_Widget)
        self.degree_label.setObjectName(u"degree_label")

        self.horizontalLayout_3.addWidget(self.degree_label)

        self.degree_checkbox = QCheckBox(self.RotateDegree_Widget)
        self.degree_checkbox.setObjectName(u"degree_checkbox")
        self.degree_checkbox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.degree_checkbox)

        self.degree_input = QLineEdit(self.RotateDegree_Widget)
        self.degree_input.setObjectName(u"degree_input")
        self.degree_input.setMinimumSize(QSize(35, 21))
        self.degree_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.degree_input)

        self.degree_btn = QPushButton(self.RotateDegree_Widget)
        self.degree_btn.setObjectName(u"degree_btn")
        self.degree_btn.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.degree_btn)


        self.verticalLayout_2.addWidget(self.RotateDegree_Widget)

        self.RotateBtn_Widget = QWidget(self.Control_Widget)
        self.RotateBtn_Widget.setObjectName(u"RotateBtn_Widget")
        self.RotateBtn_Widget.setMaximumSize(QSize(16777215, 47))
        self.horizontalLayout_4 = QHBoxLayout(self.RotateBtn_Widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.rotate_btn = QPushButton(self.RotateBtn_Widget)
        self.rotate_btn.setObjectName(u"rotate_btn")

        self.horizontalLayout_4.addWidget(self.rotate_btn)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.RotateBtn_Widget)


        self.verticalLayout_3.addWidget(self.Control_Widget)


        self.retranslateUi(RandRotateDialog)

        QMetaObject.connectSlotsByName(RandRotateDialog)
    # setupUi

    def retranslateUi(self, RandRotateDialog):
        RandRotateDialog.setWindowTitle(QCoreApplication.translate("RandRotateDialog", u"Random Rotate without losing full image", None))
        self.result_label.setText(QCoreApplication.translate("RandRotateDialog", u"Result", None))
        self.source_label.setText(QCoreApplication.translate("RandRotateDialog", u"Select Source Image Folder:", None))
        self.source_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Select", None))
        self.savepath_label.setText(QCoreApplication.translate("RandRotateDialog", u"Select Results Saving Path:", None))
        self.savepath_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Select", None))
        self.degree_label.setText(QCoreApplication.translate("RandRotateDialog", u"Select Rotate Degree:", None))
        self.degree_checkbox.setText(QCoreApplication.translate("RandRotateDialog", u"Random?", None))
        self.degree_input.setText(QCoreApplication.translate("RandRotateDialog", u"30", None))
        self.degree_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Save", None))
        self.rotate_btn.setText(QCoreApplication.translate("RandRotateDialog", u"Rotate!", None))
    # retranslateUi

