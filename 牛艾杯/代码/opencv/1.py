import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('./1.jpg',0)
cv.imshow('image',img)
plt.imshow(img[:,:,::-1])