import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('./1.jpg',0)
cv.imshow('image',img)
plt.imshow(img[:,:,::-1])
face_cascade = cv.CascadeClassifier('C:/Users/Android/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
plt.figure(figsize=(20,20))
plt.subplot(1,2,1),plt.imshow(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
img = img[...,::-1]
plt.subplot(1,2,2),plt.imshow(img),plt.title('age')
plt.show