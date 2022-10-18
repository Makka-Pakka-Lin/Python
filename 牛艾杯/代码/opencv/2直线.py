import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(123,456),(12,34,56),5)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'awei',(10,500),font,4,(13,57,91),2,cv.LINE_AA)
plt.imshow(img[:,:,::-1])
plt.title('awei'),plt.xticks([]),plt.yticks([])
plt.show()
