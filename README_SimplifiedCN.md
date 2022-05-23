# ImageCap

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

## 使用方法

目录下有多个 `.py` 文件，对应的使用方法如下：

- `ImageCap_GUI.py` ：功能最完善的版本，计算机上配置好相关环境后，利用任意 IDE 打开即可运行，支持视频流实时预览，推荐使用。
- `others\ImageCap_OpenCV.py` ：利用 OpenCV 开发的版本，未使用 PySide2 。程序运行后，需要在命令行中输入所需要的图片文件名索引号，以及需要采集图片的分辨率（`width` 与 `height` ），支持视频流实时预览。
- `gui_no_real_time.py` ：测试开发版本，用到 PySide2 进行开发，但不支持视频实时预览，需要摆好摄像头位置后，单击 "Test Frame" 按钮进行图像的手动预览。

软件运行起来后主界面如下图所示。

![img](https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/ImageCap_UI.png)

可以通过 `Width` 和 `Height` 输入框调节需要采集图像的大小。（注：预览框大小自动调整尚未实现，有待进一步更新）。默认以 `.png` 格式进行采集。通过 `index` 输入框输入图片的索引。输入 “0”，则生成的第一个文件为 "1.png"。

参数输入完毕后，单击 `Save Pref` 按钮可以保存配置信息。

`Test Frame` 按钮是一个 “历史遗留按钮”，因为在 `others\gui_no_real_time.py` 这一版的代码中，无法实现视频流的实时预览功能。但在 `ImageCap_GUI.py` 这一版中，问题得到了解决。所以现在使用这个按钮会弹出下图的提示框。

![image-20220514095227114](https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/TestFramePopup.png)

用户在拍照前需要先通过软件下方的 `Select Path` 选择路径，否则单击 `Cap!` 按钮时，会提示未选择路径。

路径选择完毕后，即可通过 `Cap!` 按钮进行连续拍照。程序的 Status 部分亦会实时对图片的保存状态进行提示。

如果拍摄意外中断，可以通过 `Index` 重新设置索引，在同一路径下继续拍照、存储照片。

<br>

## 额外的文件说明

- `QtUI\imagecap.ui` ：这是利用 PySide2 的 Qt Designer 所制作的 UI 界面文件，可用 Qt Designer 打开，修改设计。
- `imagecap_ui.py` ：利用 PySide2 的命令行工具自动生成的 `.py` 文件，用于 `ImageCap_GUI.py` 与 `gui_test_no_real_time.py` 中加载 UI 界面。