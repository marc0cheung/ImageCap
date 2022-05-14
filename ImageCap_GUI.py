# -*- coding: utf-8 -*-
# ImageCap - Using PyQt5(PySide2) GUI - Support RealTime Capture - V1.0
import cv2
import sys
from PySide2 import QtCore, QtGui, QtWidgets
import qimage2ndarray

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect
from imagecap_ui import Ui_MainWindow

imgNum = 0
FileDirectory = ''
img_width = 416
img_height = 416


class VideoPlayer(QMainWindow):

    pause = False
    video = False

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
        self.ui.TestFrameBtn.clicked.connect(self.setFrame)
        self.ui.SelcPathBtn.clicked.connect(self.chooseDir)
        self.ui.AboutBtn.clicked.connect(self.say_hello)  # 多文件的情况在这里就可以进行函数链接

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

    def setFrame(self):
        QMessageBox.information(self, 'Real-Time Capture is on', 'No Need to Use Test Frame Button.')
        '''
        success, frame = self.camera_capture.read()
        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.ui.label.setPixmap(QPixmap.fromImage(showImage))
        self.ui.label.setScaledContents(True)
        '''

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

    def say_hello(self):
        QMessageBox.information(self, 'About this software', 'Designed by Marco Cheung')

    def close_win(self):
        self.camera_capture.release()
        self.video_capture.release()
        cv2.destroyAllWindows()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
