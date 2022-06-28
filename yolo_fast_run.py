import cv2
import sys
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5x6')

PATH_TO_IMAGE = sys.path[0]+'/img/people.jpeg'
img = cv2.imread(PATH_TO_IMAGE)
results = model(img, size=1200)
results.print() 
results.save()