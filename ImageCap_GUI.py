# -*- coding: utf-8 -*-
# ImageCap - Using PyQt5(PySide2) GUI - Support RealTime Capture - V1.0

import cv2
import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
import qimage2ndarray

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect, Qt

from imagecap_ui import Ui_MainWindow
from ui_randomRotate import Ui_RandRotateDialog
from ui_fitBackground import Ui_FitBgDialog
from ImageRotate import rotate_image

imgNum = 0
FileDirectory = ''
img_width = 416
img_height = 416


class VideoPlayer(QMainWindow):

    pause = False
    video = False

    video_flip = False

    def __init__(self, width=416, height=416, fps=30):
        super().__init__()

        self.video_size = QtCore.QSize(width, height)
        self.camera_capture = cv2.VideoCapture(cv2.CAP_DSHOW)
        self.video_capture = cv2.VideoCapture()
        self.frame_timer = QtCore.QTimer()

        self.setup_camera(fps)
        self.fps = fps

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.SaveIndexBtn.clicked.connect(self.setImgNum)
        self.ui.CapBtn.clicked.connect(self.capFrame)
        self.ui.CloseBtn.clicked.connect(self.close_win)
        self.ui.SelcPathBtn.clicked.connect(self.chooseDir)
        self.ui.AboutBtn.clicked.connect(self.say_hello)

        self.ui.videoFlipCheckBox.clicked.connect(self.onVideoFlip_Changed)

    def setup_camera(self, fps):
        self.camera_capture.set(3, self.video_size.width())
        self.camera_capture.set(4, self.video_size.height())

        self.frame_timer.timeout.connect(self.display_video_stream)
        self.frame_timer.start(int(1000 // fps))

    def display_video_stream(self):
        ret, frame = self.camera_capture.read()
        if not ret:
            return False

        frame = cv2.resize(frame, (416, 416))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if self.video_flip:
            frame = cv2.flip(frame, -1, frame)

        image = qimage2ndarray.array2qimage(frame)
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def setImgNum(self):
        global imgNum
        global img_width, img_height

        imgNum = int(self.ui.index_input.toPlainText())
        img_width = int(self.ui.width_input.toPlainText())
        img_height = int(self.ui.height_input.toPlainText())
        # print("Index Now: " + str(int(self.ui.index_input.toPlainText())))
        self.ui.status_label.setText("Index\nNow\n" + str(int(self.ui.index_input.toPlainText())))
        self.ui.label.setGeometry(QRect(30, 90, img_width, img_height))

    def capFrame(self):
        global imgNum
        global FileDirectory
        global img_width, img_height

        if FileDirectory == '':
            QMessageBox.critical(self, 'Error', 'Please select save directory first.')
        else:
            success, frame = self.camera_capture.read()
            frame = cv2.resize(frame, (img_width, img_height))  # resolution setting: width x height
            show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.ui.label.setPixmap(QPixmap.fromImage(showImage))
            self.ui.label.setScaledContents(True)

            imgNum = int(imgNum) + 1
            # Write Images using imwrite
            # cv2.imwrite("D:\YOLOTraining\photos\%s.png" % (str(imgNum)), frame)
            cv2.imwrite(str(FileDirectory) + "/%s.png" % (str(imgNum)), frame)

            # print("Photo " + str(imgNum) + " Saved!")
            self.ui.status_label.setText("Photo\n" + str(imgNum) + "\nSaved!")

    def chooseDir(self):
        global FileDirectory
        FileDirectory = QFileDialog.getExistingDirectory(QMainWindow(), "Choose Save Directory")
        # print("File DIR: " + str(FileDirectory))
        self.ui.path_label.setText("Save to: " + str(FileDirectory))

    def onVideoFlip_Changed(self):
        if self.ui.videoFlipCheckBox.checkState() == Qt.Checked:
            self.video_flip = True
        elif self.ui.videoFlipCheckBox.checkState() == Qt.Unchecked:
            self.video_flip = False

    def say_hello(self):
        QMessageBox.information(self, 'About this software', 'Designed by Marco Cheung')

    def close_win(self):
        self.camera_capture.release()
        self.video_capture.release()
        cv2.destroyAllWindows()
        self.close()


class fitBackground(QDialog):
    SourceDIR = ''
    BackgroundImage = ''
    SaveDIR = ''
    BGFrame = None

    def __init__(self):
        QDialog.__init__(self)
        self.fitBgUI = Ui_FitBgDialog()
        self.fitBgUI.setupUi(self)

        self.fitBgUI.source_btn.clicked.connect(self.selectSource)
        self.fitBgUI.bg_btn.clicked.connect(self.selectBG)
        self.fitBgUI.savepath_btn.clicked.connect(self.selectSavepath)
        self.fitBgUI.color_btn.clicked.connect(self.colorSelect)
        self.fitBgUI.fit_btn.clicked.connect(self.fit)

    def selectSource(self):
        self.SourceDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Source Images Directory")
        if self.SourceDIR != '':
            self.fitBgUI.source_label.setText("Source: " + str(self.SourceDIR))

    def selectBG(self):
        self.BackgroundImage = QFileDialog.getOpenFileName(QDialog(), "Open Background Image")
        if self.BackgroundImage[0] != '':
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
        QMessageBox.critical(self, "Colour Selector Error", "Colour Selector N.A. Currently.")

    def fit(self):
        if self.BackgroundImage[0] == '':
            QMessageBox.critical(self, "Error", "Please Select a Background Image First!")
        elif self.SourceDIR == '':
            QMessageBox.critical(self, "Error", "Select a Source Folder First!")
        elif self.SaveDIR == '':
            QMessageBox.critical(self, "Error", "Select a Save Destination First!")
        else:
            BGImage = cv2.imread(self.BackgroundImage[0])
            for filename in os.listdir(self.SourceDIR):
                print(filename)
                sourceImg = cv2.imread(self.SourceDIR+'/'+filename)

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
                BGImage[0:int(fitBG_background_height) + 0, int(fitBG_background_width/2 - fitBG_ResizedWidth/2):int(fitBG_BGSetWidth)+int(fitBG_background_width/2 - fitBG_ResizedWidth/2)] = sourceImg
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

    def __init__(self):
        QDialog.__init__(self)
        self.rotateUI = Ui_RandRotateDialog()
        self.rotateUI.setupUi(self)

        self.rotateUI.source_btn.clicked.connect(self.selectSource)
        self.rotateUI.savepath_btn.clicked.connect(self.selectSavepath)
        self.rotateUI.degree_btn.clicked.connect(self.degreeSelect)
        self.rotateUI.rotate_btn.clicked.connect(self.rotate)

    def selectSource(self):
        self.SourceDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Source Images Directory")
        if self.SourceDIR != '':
            self.rotateUI.source_label.setText("Source: " + str(self.SourceDIR))

    def selectSavepath(self):
        self.SaveDIR = QFileDialog.getExistingDirectory(QDialog(), "Choose Save Directory")
        if self.SaveDIR != '':
            self.rotateUI.savepath_label.setText("Save to: " + str(self.SaveDIR))

    def degreeSelect(self):
        QMessageBox.critical(self, "Degree Selector Error", "Degree Selector N/A Currently")

    def rotate(self):
        if self.SourceDIR == '':
            QMessageBox.critical(self, "Cannot Find Source Image", "Select Source Image Folder First")
        elif self.SaveDIR == '':
            QMessageBox.critical(self, "Save Error", "Select Save Destination Folder First")
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
    player = VideoPlayer()
    fitBG = fitBackground()
    rotateIMG = rotateImage()
    player.ui.FitBgBtn.clicked.connect(fitBG.show)
    player.ui.RandRotateBtn.clicked.connect(rotateIMG.show)
    player.show()
    sys.exit(app.exec_())
