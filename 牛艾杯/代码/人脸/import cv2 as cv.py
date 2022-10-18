import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pathlib2 as pl

faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
img = cv2.imread("./1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor= 1.1,minNeighbors=8,minSize=(55, 55),flags=cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
plt.imshow(img[:,:,[2,1,0]])
plt.show()
smileCascade = cv2.CascadeClassifier("./haarcascade_smile.xml")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
smile = smileCascade.detectMultiScale(roi_gray,scaleFactor= 1.16,minNeighbors=35,minSize=(25, 25),flags=cv2.CASCADE_SCALE_IMAGE)

for (x2, y2, w2, h2) in smile:
    cv2.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)
    cv2.putText(img,'smile',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

plt.imshow(img[:,:,[2,1,0]])
plt.show()





