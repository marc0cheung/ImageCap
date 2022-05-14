# -*- coding: utf-8 -*-
# ImageCap with PySide2 GUI - Not Support Real-Time Video Stream Preview Yet. - V1.0
import sys
import cv2

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect
from imagecap_ui import Ui_MainWindow

imgNum = 0
FileDirectory = ''
img_width = 416
img_height = 416


# 继承QWidget类，以获取其属性和方法
class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.SaveIndexBtn.clicked.connect(self.setImgNum)
        self.ui.CapBtn.clicked.connect(self.capFrame)
        self.ui.CloseBtn.clicked.connect(self.closeProg)
        self.ui.TestFrameBtn.clicked.connect(self.setFrame)
        self.ui.SelcPathBtn.clicked.connect(self.chooseDir)
        self.ui.AboutBtn.clicked.connect(self.say_hello)  # 多文件的情况在这里就可以进行函数链接

    def setImgNum(self):
        global imgNum
        global img_width, img_height

        imgNum = int(self.ui.index_input.toPlainText())
        img_width = int(self.ui.width_input.toPlainText())
        img_height = int(self.ui.height_input.toPlainText())
        # print("Index Now: " + str(int(self.ui.index_input.toPlainText())))
        self.ui.status_label.setText("Index\nNow\n" + str(int(self.ui.index_input.toPlainText())))
        self.ui.label.setGeometry(QRect(30, 90, img_width, img_height))

    def closeProg(self):
        sys.exit(app.exec_())

    def setFrame(self):
        success, frame = cap.read()
        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.ui.label.setPixmap(QPixmap.fromImage(showImage))
        self.ui.label.setScaledContents(True)

    def capFrame(self):
        global imgNum
        global FileDirectory
        global img_width, img_height

        if FileDirectory == '':
            QMessageBox.critical(self, 'Error', 'Please select save directory first.')
        else:
            success, frame = cap.read()
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


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    cap = cv2.VideoCapture(0)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
    # 注意，在PySide6中，需要使用app.exec()
    # sys.exit(app.exec())
