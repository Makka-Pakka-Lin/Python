import numpy as np
import cv2
#调用USB摄像头
cap = cv2.VideoCapture(-1)
while True:
    #从摄像头读取图片
    sucess, img = cap.read()
    #转为灰度图片
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #显示摄像头，背景是灰度
    #cv2.imshow("img", gray)
 
    #保持画面的持续。
    k = cv2.waitKey(3)
    cv2.imwrite("image1.jpg", img)
    imageFn = 'image1.jpg'
    break
 
#关闭摄像头
cap.release()