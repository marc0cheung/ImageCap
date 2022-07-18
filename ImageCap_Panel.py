# -*- coding: utf-8 -*-
# ImageCap - Using PyQt5(PySide2) GUI - Support RealTime Capture

import os
import re
import sys
import cv2
import numpy

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog, QColorDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect, Qt

from ui_imagecap_panel import Ui_MainWindow
from ui_randomRotate import Ui_RandRotateDialog
from ui_fitBackground import Ui_FitBgDialog
from ImageRotate import rotate_image, rotateImage_FixedDegree

# IF RUNNING ON macOS, Uncomment Line 19 (Below)
os.environ['QT_MAC_WANTS_LAYER'] = '1'


class MainPanel(QMainWindow):
    video_flip = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class fitBackground(QDialog):
    SourceDIR = ''
    BackgroundImage = ''  # This is a List due to Pyside2 File Reader
    BGDIR = ''
    SaveDIR = ''
    BGFrame = None
    selectedColor = None

    def __init__(self):
        QDialog.__init__(self)
        self.fitBgUI = Ui_FitBgDialog()
        self.fitBgUI.setupUi(self)

        self.fitBgUI.source_btn.clicked.connect(self.selectSource)
        self.fitBgUI.bg_btn.clicked.connect(self.selectBG)
        self.fitBgUI.savepath_btn.clicked.connect(self.selectSavepath)
        self.fitBgUI.colorDialogBtn.clicked.connect(self.colorSelect)
        self.fitBgUI.fit_btn.clicked.connect(self.fit)

    def selectSource(self):
        self.SourceDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Source Images Directory")
        if self.SourceDIR != '':
            self.fitBgUI.source_label.setText("Source: " + str(self.SourceDIR))

    def selectBG(self):
        self.BackgroundImage = QFileDialog.getOpenFileName(QDialog(), "Open Background Image")
        if self.BackgroundImage[0] != '':
            self.BGDIR = self.BackgroundImage[0]
            self.fitBgUI.bg_label.setText("BG: " + str(self.BackgroundImage[0]))
            frame = cv2.imread(self.BackgroundImage[0])
            self.BGFrame = frame
            show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.fitBgUI.result_label.setPixmap(QPixmap.fromImage(showImage))

    def selectSavepath(self):
        self.SaveDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Save Directory")
        if self.SaveDIR != '':
            self.fitBgUI.savepath_label.setText("Save to: " + str(self.SaveDIR))

    def colorSelect(self):
        # Image Resolution: 416 * 416, 3 channels, [:, :, 0] for Blue, [:, :, 1] for Green, [:, :, 2] for Red
        # Decode RGB values from color_input_box
        self.selectedColor = QColorDialog.getColor().getRgb()

        redValue = int(self.selectedColor[0])
        greenValue = int(self.selectedColor[1])
        blueValue = int(self.selectedColor[2])

        # Create a new pure color image for background
        imgGenerated = numpy.zeros([416, 416, 3], numpy.uint8)

        imgGenerated[:, :, 2] = numpy.ones([416, 416]) * redValue  # Red Channel
        imgGenerated[:, :, 1] = numpy.ones([416, 416]) * greenValue  # Green Channel
        imgGenerated[:, :, 0] = numpy.ones([416, 416]) * blueValue  # Blue Channel

        # Show Generated Background in the programme window
        show = cv2.cvtColor(imgGenerated, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.fitBgUI.result_label.setPixmap(QPixmap.fromImage(showImage))

        # Save Generated Background and pass its path to BGDIR for further usage in function 'fit'
        cv2.imwrite("./Generated_BG.png", imgGenerated)
        self.BGDIR = "./Generated_BG.png"
        self.fitBgUI.bg_label.setText("BG: Use Generated Background Now.")
        self.fitBgUI.colorRGBLabel.setText(str(self.selectedColor))

    def fit(self):
        if self.BGDIR == '':
            QMessageBox.critical(self, "Error", "Please Select a Background Image First!")
        elif self.SourceDIR == '':
            QMessageBox.critical(self, "Error", "Select a Source Folder First!")
        elif self.SaveDIR == '':
            QMessageBox.critical(self, "Error", "Select a Save Destination First!")
        else:
            BGImage = cv2.imread(self.BGDIR)
            for filename in os.listdir(self.SourceDIR):
                print(filename)
                sourceImg = cv2.imread(self.SourceDIR + '/' + filename)

                # Get Image Shape
                fitBG_imgWidth = sourceImg.shape[1]
                fitBG_imgHeight = sourceImg.shape[0]
                fitBG_background_width = BGImage.shape[1]
                fitBG_background_height = BGImage.shape[0]

                # Get Source Image Ratio, get target resized width
                # according to the height of BGFrame
                fitBG_ImgRatio = fitBG_imgHeight / fitBG_imgWidth
                fitBG_BGSetWidth = fitBG_background_height / fitBG_ImgRatio
                fitBG_ResizedWidth = int(fitBG_BGSetWidth)
                fitBG_ResizedHeight = int(fitBG_background_height)

                # Resize the Source Image
                sourceImg = cv2.resize(sourceImg, (fitBG_ResizedWidth, fitBG_ResizedHeight))

                # Insert the resized remote image to background
                BGImage[0:int(fitBG_background_height) + 0,
                int(fitBG_background_width / 2 - fitBG_ResizedWidth / 2):int(fitBG_BGSetWidth) + int(
                    fitBG_background_width / 2 - fitBG_ResizedWidth / 2)] = sourceImg
                result = BGImage

                # Show and Save the Target Images

                # Show Results in CV2 GUI
                # cv2.imshow("Test", result)
                # cv2.waitKey(1)  # no keyboard input in 1ms then continue

                # Show Results in Qt GUI
                show = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.fitBgUI.result_label.setPixmap(QPixmap.fromImage(showImage))
                cv2.waitKey(1)

                cv2.imwrite(self.SaveDIR + '/%s' % filename, result)


class rotateImage(QDialog):
    SourceDIR = ''
    SaveDIR = ''
    randomRotate = True
    rotateDegree = 30.0

    def __init__(self):
        QDialog.__init__(self)
        self.rotateUI = Ui_RandRotateDialog()
        self.rotateUI.setupUi(self)

        self.rotateUI.source_btn.clicked.connect(self.selectSource)
        self.rotateUI.savepath_btn.clicked.connect(self.selectSavepath)
        self.rotateUI.degree_btn.clicked.connect(self.degreeSelect)
        self.rotateUI.rotate_btn.clicked.connect(self.rotate)

        self.rotateUI.degree_checkbox.clicked.connect(self.onRandomRotateChanged)

    def selectSource(self):
        self.SourceDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Source Images Directory")
        if self.SourceDIR != '':
            self.rotateUI.source_label.setText("Source: " + str(self.SourceDIR))

    def selectSavepath(self):
        self.SaveDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Save Directory")
        if self.SaveDIR != '':
            self.rotateUI.savepath_label.setText("Save to: " + str(self.SaveDIR))

    def degreeSelect(self):
        if re.match("^[-+]?[0-9]|^[-+]?[0-9]+\.[0-9]+$", self.rotateUI.degree_input.toPlainText(), flags=0) is None:
            QMessageBox.critical(self, "Degree Input Error", "Cannot Match Degree Value.")
        else:
            self.rotateDegree = float(self.rotateUI.degree_input.toPlainText())

    def onRandomRotateChanged(self):
        if self.rotateUI.degree_checkbox.checkState() == Qt.Checked:
            self.randomRotate = True
            self.rotateUI.degree_input.setEnabled(False)
            self.rotateUI.degree_btn.setEnabled(False)
        elif self.rotateUI.degree_checkbox.checkState() == Qt.Unchecked:
            self.randomRotate = False
            self.rotateUI.degree_input.setEnabled(True)
            self.rotateUI.degree_btn.setEnabled(True)

    def rotate(self):
        if self.SourceDIR == '':
            QMessageBox.critical(self, "Cannot Find Source Image", "Select Source Image Folder First")
        elif self.SaveDIR == '':
            QMessageBox.critical(self, "Save Error", "Select Save Destination Folder First")
        elif not self.randomRotate:
            for filename in os.listdir(self.SourceDIR):
                result_FixedDegree = rotateImage_FixedDegree(str(self.SourceDIR), filename, float(self.rotateDegree))

                show = cv2.cvtColor(result_FixedDegree, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.rotateUI.result_label.setPixmap(QPixmap.fromImage(showImage))
                cv2.waitKey(1)

                cv2.imwrite(self.SaveDIR + "/%s" % "FixedRotated_" + filename, result_FixedDegree)
        else:
            for filename in os.listdir(self.SourceDIR):
                result = rotate_image(str(self.SourceDIR), filename)

                show = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.rotateUI.result_label.setPixmap(QPixmap.fromImage(showImage))
                cv2.waitKey(1)

                cv2.imwrite(self.SaveDIR + "/%s" % "rotated_" + filename, result)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainPanel = MainPanel()
    fitBG = fitBackground()
    rotateIMG = rotateImage()
    mainPanel.ui.FitBgBtn.clicked.connect(fitBG.show)
    mainPanel.ui.RandRotateBtn.clicked.connect(rotateIMG.show)
    mainPanel.show()
    sys.exit(app.exec_())
