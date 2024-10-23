#*在屏幕中显示识别的结果*
#from camera_android import *
#import cv2
#import numpy as np
from MyModel import *
from picture import *
from cvs import *
import os

#读取拍摄的图片
RGB_img=cv2.imread(imageFn)
blank_img = np.zeros(shape=(RGB_img.shape[0],RGB_img.shape[1],3), dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX

# 添加水印的文字内容
text1 = "number:"+lable_list[w]
cv2.putText(blank_img,text=text1,org=(100, 100),
            fontFace=font,fontScale= 2,
            color=(255,255,255),thickness=4,lineType=cv2.LINE_4)
blended = cv2.addWeighted(src1=RGB_img, alpha=0.7,
                          src2=blank_img, beta=1, gamma = 2)
cv2.imwrite("blended1.jpg",blended)                          
cap = cvs.VideoCapture("blended1.jpg")
blended1 = cap.read()
cap.imshow(blended1)
os.remove("blended1.jpg")