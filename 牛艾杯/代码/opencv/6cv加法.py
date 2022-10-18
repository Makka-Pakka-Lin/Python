import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread("1.jpg")
img2 = cv.imread("2.jpg")
img3 = cv.add(img1,img2)
img4 = img1+img2
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=(100))
axes[0].imshow(img3[:,:,::-1])
axes[0].setset_title("cv的加法")
axes[1].imshow(img4[:,:,::-1])
axes[1].setset_title("jiji")
plt.show()







