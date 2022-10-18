import numpy as np
import cv2 as cv
import os
import time
from matplotlib import pyplot as plt

yolo_dir = './1.jpg'  
weightsPath = os.path.join(yolo_dir, './yolov3/yolov3.weights')  
configPath = os.path.join(yolo_dir, './yolov3/yolov3.cfg')  
labelsPath = os.path.join(yolo_dir, './yolov3/coco.names')  
imgPath = os.path.join(yolo_dir, './yolov3/kite.jpg')  

CONFIDENCE = 0.5  
THRESHOLD = 0.4  

net = cv.dnn.readNetFromDarknet(configPath, weightsPath)  
print("[INFO] loading YOLO from disk...")  

img = cv.imread(imgPath)
blobImg = cv.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)   
net.setInput(blobImg)  

outInfo = net.getUnconnectedOutLayersNames()
start = time.time()
layerOutputs = net.forward(outInfo)  
end = time.time()
print("[INFO] YOLO took {:.6f} seconds".format(end - start)) 

(H, W) = img.shape[:2] 
boxes = [] 
confidences = [] 
classIDs = []


for out in layerOutputs:  
    for detection in out:  
        
        scores = detection[5:] 
        classID = np.argmax(scores)  
        confidence = scores[classID]  

        if confidence > CONFIDENCE:
            box = detection[0:4] * np.array([W, H, W, H])  
            (centerX, centerY, width, height) = box.astype("int")
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)

idxs = cv.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)

with open(labelsPath, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')
    
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8") 
if len(idxs) > 0:
    for i in idxs.flatten(): 
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])

        color = [int(c) for c in COLORS[classIDs[i]]]
        cv.rectangle(img, (x, y), (x+w, y+h), color, 2)  
        text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
        cv.putText(img, text, (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  

img3=img[:,:,::-1]
plt.figure(figsize=(20,20))
plt.imshow(img3)











