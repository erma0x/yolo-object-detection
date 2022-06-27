# Object detection using YOLO deep learning with OpenCV and Python 

![](output/result.jpeg?raw=true)

OpenCV `dnn` module supports running inference on pre-trained deep learning models from popular frameworks like Caffe, Torch and TensorFlow. 

 ## Dependencies
  * opencv
  * numpy
  
`pip install numpy opencv-python`

**Note: Compatability with Python 2.x is not officially tested.**

 ## YOLO (You Only Look Once)
 
 Download the pre-trained YOLO v3 weights file:
 
 `$ wget https://pjreddie.com/media/files/yolov3.weights`
 
 Provided all the files are in the current directory, below command will apply object detection on the input image `desk.jpeg`.

 ## Test with an image
 
 `$ python3 image_yolo.py --image img/desk.jpeg --config yolov3.cfg --weights yolov3.weights --classes yolov3.txt -o result.jpeg`
 
  ## Test with a videocamera

 `$ python3 video_yolo.py --config yolov3.cfg --weights yolov3.weights --classes yolov3.txt`