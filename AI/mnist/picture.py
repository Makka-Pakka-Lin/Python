#*对拍摄的数字图片预处理*
import cv2
from usbcamera import *
import imutils

img = cv2.imread(imageFn)                  #读取图片，imageFn为图片路径
img = imutils.resize(img,width=195)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     #灰度图
#cv2.imwrite("11.jpg",gray_img)

#创建空白数组
for row in range(146):
    for col in range(195):
        gray_img[row][col] = 255 - gray_img[row][col]#反色
# 二值化，(127,255)为阈值
retval,bit_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
bit_img = cv2.resize(bit_img, (28,28), interpolation= cv2.INTER_AREA)
retval,bit_img = cv2.threshold(bit_img, 20, 255, cv2.THRESH_BINARY)

#cv2.imwrite("77.jpg",bit_img)                       #保存图片
