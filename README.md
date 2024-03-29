# Yolo Object Detection
#### Object detection using yolo deep learning models with opencv and python 

![](output/result.jpeg?raw=true)

 ## Dependencies
  * opencv
  * numpy
  
`pip install numpy opencv-python`

**Note: Compatability with Python 2.x is not officially tested.**

 ## YOLO (You Only Look Once)
 
 Download one of the pre-trained YOLO weights file from the following link (example with yolov5n6.pt):
 
 `wget https://github.com/ultralytics/yolov5/releases/download/v6.1/yolov5n6.pt ./models/`
 
 `https://github.com/ultralytics/yolov5/releases`

 Provided all the files are in the current directory, below command will apply object detection on the input image `desk.jpeg`.

 ## Test with an image
 
 `$ python3 image_yolo.py --image img/desk.jpeg --config yolov3.cfg --weights yolov3.weights --classes classes.txt -o result.jpeg`
 
  ## Test with a videocamera

 `$ python3 video_yolo.py --weights yolov5n6.pt --classes classes.txt`
