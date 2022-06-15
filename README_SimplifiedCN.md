# ImageCap

语言选择： [English](https://github.com/marc0cheung/ImageCap/blob/main/README.md) | 简体中文

<br>

<br>

## 项目依赖

```python
# Use pip to install following packages
pip install opencv-python
pip install pyside2
pip install qimage2ndarray

# import
import cv2
import sys
from PySide2 import QtCore, QtGui, QtWidgets
import qimage2ndarray

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect
from imagecap_ui import Ui_MainWindow
```

<br>

## 程序介绍

ImageCap 是基于 PySide2 和 OpenCV 开发的神经网络训练素材采集程序。

在训练神经网络的过程中，需要采集大量图片，而中途经常遇到采集中断的情况。ImageCap 支援自编图片名索引，在采集流程终端后还可以继续之前的索引继续拍摄。

通过修改代码，可以兼容本地USB摄像头、远程网络摄像头等。

ImageCap 还支援自选图片保存路径，以及视频流实时预览功能。

<br>

## 使用方法之如何拍摄照片

目录下有多个 `.py` 文件，对应的使用方法如下：

- `ImageCap_GUI.py` ：功能最完善的版本，计算机上配置好相关环境后，利用任意 IDE 打开即可运行，支持视频流实时预览，推荐使用。
- `others\ImageCap_OpenCV.py` ：利用 OpenCV 开发的版本，未使用 PySide2 。程序运行后，需要在命令行中输入所需要的图片文件名索引号，以及需要采集图片的分辨率（`width` 与 `height` ），支持视频流实时预览。
- `gui_no_real_time.py` ：测试开发版本，用到 PySide2 进行开发，但不支持视频实时预览，需要摆好摄像头位置后，单击 "Test Frame" 按钮进行图像的手动预览。

软件运行起来后主界面如下图所示。

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/ImageCap_UI.png" alt="img" style="zoom:67%;" /></div>

可以通过 `Width` 和 `Height` 输入框调节需要采集图像的大小。（注：预览框大小自动调整尚未实现，有待进一步更新）。默认以 `.png` 格式进行采集。通过 `index` 输入框输入图片的索引。输入 “0”，则生成的第一个文件为 "1.png"。

参数输入完毕后，单击 `Save Pref` 按钮可以保存配置信息。

用户在拍照前需要先通过软件下方的 `Select Path` 选择路径，否则单击 `Cap!` 按钮时，会提示未选择路径。

路径选择完毕后，即可通过 `Cap!` 按钮进行连续拍照。程序的 Status 部分亦会实时对图片的保存状态进行提示。

如果拍摄意外中断，可以通过 `Index` 重新设置索引，在同一路径下继续拍照、存储照片。



如果摄像头的安装方向是反过来的（比如一些工业摄像头的安装位置），那么可以勾选界面中的 Video Flip 按钮来得到正向的图像。

<br>

## 使用说明之如何使用随机旋转功能

训练神经网络常需要不同角度的目标物照片进行训练，此时可以使用这个功能将照片进行无裁剪的随机旋转。效果图如下：

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/randomRotateResult.png" alt="randomRotateResult" style="zoom:67%;" /></div>



此功能页面的示意图如下，只需要选择存放原始图片的路径，选择保存旋转结果的路径，单击 Rotate 按钮即可开始随机旋转，实时的旋转结果可以在窗口中实时看到。固定旋转角度的功能还在开发中，ImageCap 的下一个版本将更新此功能。

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/randomRotateWindow.png" alt="randomRotateWindow" style="zoom:67%;" /></div>

<br>

## 使用说明之如何使用套用背景功能

在生产线上采集的目标物图片是经过裁剪的，此时需要将其缩放到 416 * 416 的图片中。如果利用 PhotoShop 一张张处理，会十分麻烦。这一个功能通过计算原始目标物图片的比例，并自动计算将其等比例缩放到高为 416px 的情况下，对应的宽度像素值。在经过缩放后，将目标物图片移动到背景图片上，实现如下图所示的效果。

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/fitBackgroundResult.png" alt="fitBackgroundResult" style="zoom:67%;" /></div>



此功能页面的示意图如下所示，只需要选择存放目标物图片的路径、选择一张纯色或任意需要使用的背景图片以及选择图片输出路径，即可开始自动按比例将目标物套用到背景图片上。

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/fitBackgroundWindow.png" alt="fitBackgroundWindow" style="zoom:67%;" /></div>



目前，需要用户自己通过 MS Paint 制作一张尺寸为 416 * 416 （当前必须为 416 * 416）的背景图片，然后在程序中选择这张图片。自定义选择纯色背景的功能、以及自定义背景尺寸的功能还没有开发完毕，这些功能将在下一个版本的 ImageCap 中放出。

<br>

## 额外的文件说明

- `QtUI\imagecap.ui` ：这是利用 PySide2 的 Qt Designer 所制作的 UI 界面文件，可用 Qt Designer 打开，修改设计。
- `imagecap_ui.py` ：利用 PySide2 的命令行工具自动生成的 `.py` 文件，用于 `ImageCap_GUI.py` 与 `gui_test_no_real_time.py` 中加载 UI 界面。
- `ui_fitBackground.py` : 利用 PySide2 的命令行工具自动生成的 `.py` 文件，用于 `ImageCap_GUI.py` 中的套用背景功能页面加载 UI 界面。
- `ui_randomRotate.py` : 利用 PySide2 的命令行工具自动生成的 `.py` 文件，用于 `ImageCap_GUI.py` 中的随机旋转功能页面加载 UI 界面。
- `ImageRotate.py` ： 随机旋转图片所使用到的函数文件