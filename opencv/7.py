import numpy as np
from PIL import Image
import cv2

imgfile = "3.jpg"
OriginalPic = np.array(Image.open(imgfile).convert('L'), dtype=np.uint8)
img = np.zeros((OriginalPic.shape[0]+2, OriginalPic.shape[1]+2), np.uint8)

#########  制造遍历图像  ###################
for i in range(1, img.shape[0]-1):
    for j in range(1, img.shape[1]-1):
        img[i][j] = OriginalPic[i-1][j-1]

LaplacePic = np.zeros((OriginalPic.shape[0], OriginalPic.shape[1]), dtype=np.uint8)
kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
for i in range(0, LaplacePic.shape[0]):
    for j in range(0, LaplacePic.shape[1]):
        LaplacePic[i][j] = abs(np.sum(np.multiply(kernel, img[i:i+3, j:j+3])))

cv2.imshow("Original", OriginalPic)
cv2.imshow("Laplace", LaplacePic)
cv2.imwrite("old.jpg", OriginalPic)
cv2.imwrite("new.jpg", LaplacePic)
cv2.waitKey(0)

