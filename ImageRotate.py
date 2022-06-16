# -*- coding: utf-8 -*-
# Rotate Images for certain(or random) degrees
# -*-coding:utf-8-*-
"""
File Name: ImageRotate.py
Program IDE: PyCharm
Date: 20220616
Create File By Author: Marco Cheung
"""
import random

import cv2 as cv
import numpy as np


def rotate_image(image_path: str, filename: str):
    """
    Two ways of rotate images
    1. Angle-specific rotation functions, but only special angle rotations like 90, 180 and 270 are supported.
    2. The arbitrary angle rotation function, which requires the rotation matrix M, has two ways of obtaining
    the rotation matrix M: manually configured (which allows for a rotated image without cropping) and obtained
    by the built-in function
    :param filename: pass filename into this function
    :param image_path: pass image_path
    :return: Null
    """

    img = cv.imread(image_path + '/' + filename, cv.IMREAD_COLOR)
    # cv.imshow('input', img)

    h, w, c = img.shape

    # ### Get Rotated Images with cropping #######
    # ##########Set the rotation matrix M manually#################
    # Define Empty Matrix
    M = np.zeros((2, 3), dtype=np.float32)

    # Set Rotate Angle
    alpha = np.cos(np.pi / random.randint(1, 10))
    beta = np.sin(np.pi / random.randint(1, 10))
    print('alpha: ', alpha)
    # Initialising the rotation matrix
    M[0, 0] = alpha
    M[1, 1] = alpha
    M[0, 1] = beta
    M[1, 0] = -beta

    cx = w / 2
    cy = h / 2

    tx = (1 - alpha) * cx - beta * cy
    ty = beta * cx + (1 - alpha) * cy

    M[0, 2] = tx
    M[1, 2] = ty

    # The built-in function gets the rotation matrix M. Positive values indicate counterclockwise rotation, assuming
    # that the upper left corner is the origin of the coordinates
    M = cv.getRotationMatrix2D((w / 2, h / 2), 45, 1)
    # Start rotation, rotation at any angle
    result_cropped = cv.warpAffine(img, M, (w, h))

    # Displays the results of rotating images with the rotation angle set manually
    # result = np.hstack((img, result))
    # cv.imwrite('images/rotate2.jpg', result)
    # cv.imshow('rotate center', result)

    #  #######Get the rotated image without cropping#########
    #  Define Empty Matrix
    M = np.zeros((2, 3), dtype=np.float32)
    # Set rotation angle
    alpha = np.cos(np.pi / random.choice([random.randint(-10,-1),random.randint(1,10)]))
    beta = np.sin(np.pi / random.choice([random.randint(-10,-1),random.randint(1,10)]))
    print('alpha: ', alpha)
    # Initialising the rotation matrix
    M[0, 0] = alpha
    M[1, 1] = alpha
    M[0, 1] = beta
    M[1, 0] = -beta
    # Center Point Coordinate of Image
    cx = w / 2
    cy = h / 2
    #
    # Alpha of Width and Height
    tx = (1 - alpha) * cx - beta * cy
    ty = beta * cx + (1 - alpha) * cy
    M[0, 2] = tx
    M[1, 2] = ty
    #
    # The Height and Width of Image after rotation
    rotated_w = int(h * np.abs(beta) + w * np.abs(alpha))
    rotated_h = int(h * np.abs(alpha) + w * np.abs(beta))
    #
    # Centre position after rotation
    M[0, 2] += rotated_w / 2 - cx
    M[1, 2] += rotated_h / 2 - cy
    #
    result = cv.warpAffine(img, M, (rotated_w, rotated_h))
    result = cv.resize(result, (416, 416))

    return result

    # cv.imshow('result', result)
    # cv.imwrite(str(save_path) + '/%s' % str(filename), result)
    #
    # show = cv.cvtColor(result, cv.COLOR_BGR2RGB)
    # showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
    # rotateIMG.rotateUI.result_label.setPixmap(QPixmap.fromImage(showImage))
    #
    # cv.waitKey(1)
    # cv.destroyAllWindows()


def rotateImage_FixedDegree(image_path: str, filename: str, degree: float):
    img = cv.imread(image_path + '/' + filename, cv.IMREAD_COLOR)
    # cv.imshow('input', img)

    h, w, c = img.shape

    #  #######Get the rotated image without cropping#########
    #  Define Empty Matrix
    M = np.zeros((2, 3), dtype=np.float32)
    # Set rotation angle
    alpha = np.cos(np.pi / degree)
    beta = np.sin(np.pi / degree)
    print('alpha: ', alpha)
    # Initialising the rotation matrix
    M[0, 0] = alpha
    M[1, 1] = alpha
    M[0, 1] = beta
    M[1, 0] = -beta
    # Center Point Coordinate of Image
    cx = w / 2
    cy = h / 2
    #
    # Alpha of Width and Height
    tx = (1 - alpha) * cx - beta * cy
    ty = beta * cx + (1 - alpha) * cy
    M[0, 2] = tx
    M[1, 2] = ty
    #
    # The Height and Width of Image after rotation
    rotated_w = int(h * np.abs(beta) + w * np.abs(alpha))
    rotated_h = int(h * np.abs(alpha) + w * np.abs(beta))
    #
    # Centre position after rotation
    M[0, 2] += rotated_w / 2 - cx
    M[1, 2] += rotated_h / 2 - cy
    #
    result_FixedDegree = cv.warpAffine(img, M, (rotated_w, rotated_h))
    result_FixedDegree = cv.resize(result_FixedDegree, (416, 416))

    return result_FixedDegree
