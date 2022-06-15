# -*- coding: utf-8 -*-
# Rotate Images for certain(or random) degrees
# -*-coding:utf-8-*-
"""
File Name: ImageRotate.py
Program IDE: PyCharm
Date: 20220510
Create File By Author: Marco Cheung
"""
import cv2 as cv
import numpy as np
import os
import random
from PySide2.QtGui import QImage, QPixmap


def rotate_image(image_path: str, save_path: str, rotateIMG=None):
    """
    旋转图像，介绍两种旋转方式。
    1、特定角度旋转函数，但是只支持90、180、270这样特殊的角度旋转。
    2、任意角度旋转函数，需要旋转矩阵M，有两种获取旋转矩阵M的方式：手动配置（可以实现没有裁剪后的旋转图像）和内置函数获取
    :param rotateIMG: Dunno What to do
    :param save_path: Save Path
    :param image_path: 传入的图像文件
    :return: 没有返回值
    """

    for filename in os.listdir(image_path):
        img = cv.imread(image_path + '/' + filename, cv.IMREAD_COLOR)
        # cv.imshow('input', img)

        h, w, c = img.shape

        # ###以下旋转方式获取的都是裁剪后的旋转图像#######
        # ##########手动设置旋转矩阵M#################
        # 定义空矩阵
        M = np.zeros((2, 3), dtype=np.float32)

        # 设定旋转角度
        alpha = np.cos(np.pi / random.randint(1, 10))
        beta = np.sin(np.pi / random.randint(1, 10))
        print('alpha: ', alpha)
        # 初始化旋转矩阵
        M[0, 0] = alpha
        M[1, 1] = alpha
        M[0, 1] = beta
        M[1, 0] = -beta

        # 图片中心点坐标
        cx = w / 2
        cy = h / 2

        # 变化的宽高
        tx = (1 - alpha) * cx - beta * cy
        ty = beta * cx + (1 - alpha) * cy

        M[0, 2] = tx
        M[1, 2] = ty

        # 内置函数获取旋转矩阵M，正值表示逆时针旋转，假设左上角是坐标原点
        M = cv.getRotationMatrix2D((w / 2, h / 2), 45, 1)
        # 执行旋转, 任意角度旋转
        result = cv.warpAffine(img, M, (w, h))

        # 显示手动设置旋转角度的旋转图像结果
        # result = np.hstack((img, result))
        # cv.imwrite('images/rotate2.jpg', result)
        # cv.imshow('rotate center', result)

        #  #######获取没有裁剪的旋转图像#########
        #  定义空矩阵
        M = np.zeros((2, 3), dtype=np.float32)
        # 设定旋转角度
        alpha = np.cos(np.pi / random.choice([random.randint(-10,-1),random.randint(1,10)]))
        beta = np.sin(np.pi / random.choice([random.randint(-10,-1),random.randint(1,10)]))
        print('alpha: ', alpha)
        # 初始化旋转矩阵
        M[0, 0] = alpha
        M[1, 1] = alpha
        M[0, 1] = beta
        M[1, 0] = -beta
        # 图片中心点坐标
        cx = w / 2
        cy = h / 2
        #
        # # 变化的宽高
        tx = (1 - alpha) * cx - beta * cy
        ty = beta * cx + (1 - alpha) * cy
        M[0, 2] = tx
        M[1, 2] = ty
        #
        # # 旋转后的图像高、宽
        rotated_w = int(h * np.abs(beta) + w * np.abs(alpha))
        rotated_h = int(h * np.abs(alpha) + w * np.abs(beta))
        #
        # # 移动后的中心位置
        M[0, 2] += rotated_w / 2 - cx
        M[1, 2] += rotated_h / 2 - cy
        #
        result = cv.warpAffine(img, M, (rotated_w, rotated_h))
        result = cv.resize(result, (416, 416))
        # cv.imshow('result', result)
        cv.imwrite(str(save_path) + '/%s' % str(filename), result)

        show = cv.cvtColor(result, cv.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        rotateIMG.rotateUI.result_label.setPixmap(QPixmap.fromImage(showImage))

        # cv.waitKey(0)
        # cv.destroyAllWindows()
