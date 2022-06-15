# ImageCap
**Select Language**: English | [Simplified Chinese](https://github.com/marc0cheung/ImageCap/blob/main/README_SimplifiedCN.md) 

<br>

<br>

ImageCap is a Python Software for rapid image capture for neural network training. Support ratio-protected image resize and image rotate. GUI designed and generated by PySide2 (PyQt5). 

<div align=center><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/ImageCap_UI.png" alt="Mainpage_of_ImageCap" width="400px" /></div>

<br>

## Package Requirements

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

## How To Use ImageCap to Take Photos

- Use `Width` and `Height` input box to adjust the size(resolution, px) of the capture image. 
  P.S. Preview Box **DO NOT** support Auto-Resize currently, so use resolution other than 416*416 might cause GUI bugs, pending to be solved in the next update version...
- Use `.png` format to capture images by default. 
- Use `index` input box to input the index of the image. 
  e.g. Input "0", the first capture image filename will be `1.png` 
- Click `Save Pref` Button to save the configs above.

<br>

- Before using `Cap!` to get a photo, user needs to select a saving path by clicking the `Select Path` Button below the Application Window. Otherwise an Error Box would pop up and remind the user that "Please select a saving directory first"
- After selecting the saving path, you can click `Cap!` to take photos. The `Status` part of the application will also remind user of the saving status of the photos.
- If the capture process is unexpectedly interrupted, you can reset the index with `Index` to continue taking and storing photos in the same path.

<br>

- If the camera is mounted in the opposite direction (as in the case of some industrial cameras), then the `Video Flip` Check Box in the interface can be ticked to get a positive image.

<br>

## Use ImageCap to Rotate Images Randomly

To train a neural network, it is often necessary to take photos of the target at different angles, so this function can be used to rotate the photos randomly without cropping. The results of this feature are as follows.

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/randomRotateResult.png" alt="randomRotateResult" width="600px" /></div>

<br>

This function page is illustrated on the Picture below. Simply select the path where the original image is stored, select the path where the rotation results will be saved and click the Rotate button to start a random rotation, the live rotation results can be seen in the window in real time. The ability to fix the rotation angle is still under development and will be updated in the next version of ImageCap.

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/randomRotateWindow.png" alt="randomRotateWindow" width="300px" /></div>

<br>

## Fit Background Using ImageCap

The images of the targets collected on the production line are always cropped and need to be scaled down to 416 * 416 images. This would be very cumbersome if PhotoShop was used to process them one by one. This function calculates the scale of the original target image and automatically calculates the pixel value of the width if it is scaled equally to a height of 416px. After scaling, the target image is moved to the background image to achieve the effect shown below.

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/fitBackgroundResult.png" alt="fitBackgroundResult" width="600px" /></div>

<br>

The function page is shown below. Simply select the path where the target image is stored, select a solid colour or any background image to be used and select the image output path to start automatically applying the target to the background image to scale.

<div align="center"><img src="https://github.com/marc0cheung/ImageCap/raw/main/readme_assets/fitBackgroundWindow.png" alt="fitBackgroundWindow" width="300px" /></div>

<br>

Currently, you need to create your own background image in MS Paint with a size of 416 * 416 (currently it must be 416 * 416) and then select this image in the program. The ability to custom select a solid colour background, and the ability to customise the size of the background is not yet developed and will be released in the next version of ImageCap.

<br>

## Other Files in the Project Folder

- `QtUI\imagecap.ui`: A UI design file made by Qt Designer of PySide2, you can open it with Qt Designer and adjust the design.
- `imagecap_ui.py` :  A `.py` file that includes UI Design generated by the `pyside2-uic` command line tool. Use to load UI interfaces in  `ImageCap_GUI.py` and `gui_test_no_real_time.py` 

- `ui_fitBackground.py` : A `.py` file automatically generated using PySide2's command line tools for loading the UI interface with the fit background function page in `ImageCap_GUI.py`.
- `ui_randomRotate.py` : A `.py` file automatically generated using PySide2's command line tools for loading the UI interface for the random rotate function page in `ImageCap_GUI.py`.
- `ImageRotate.py` : The function file used to randomly rotate the image
