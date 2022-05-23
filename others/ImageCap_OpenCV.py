# -*- coding: utf-8 -*-
# ImageCap - Using OpenCV GUI - V1.0
import cv2


def main():
    # Activate Local USB Camera
    cam = cv2.VideoCapture(0)
    global img_width, img_height
    while True:
        ret, frame = cam.read()
        frame = cv2.resize(frame, (int(img_width), int(img_height)))  # Set the photo size you want
        cv2.imshow("ImageCap", frame)
        # waitKey(1) keep waiting
        key = cv2.waitKey(1)
        # Mouse Left-Click Btn Event, frame pass to 'param' of OnMouseAction()
        cv2.setMouseCallback("ImageCap", onMouseAction, frame)
        # Press ESC on Keyboard to Stop the Programme
        if key & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


def onMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global imgNum
        imgNum = int(imgNum) + 1

        # Write Images using imwrite
        cv2.imwrite("D:\YOLOTraining\photos\%s.png" % (str(imgNum)), param)

        print("Photo " + str(imgNum) + " Saved!")


# Input ImgNum
print('\nImageCap: A Python-Based Photo Collector for DNN Training')
print('Use 0 for ImgNum, then get 1.png, 2.png, 3.png, ... , n.png')
imgNum = input('\nInput ImgNum(Start): ')
img_width = input('\nInput ImgWidth: ')
img_height = input('\nInput imgHeight: ')
main()
