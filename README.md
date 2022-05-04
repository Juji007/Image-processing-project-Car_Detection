# Vehicle Detection
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

The Project
---

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video or single image and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

How to use
---
* first downlowd the image data required for car detection training https://www.kaggle.com/datasets/brsdincer/vehicle-detection-image-set
and extract it in the code folder
* run anaconda cmd and run Vechicale_Detector.py with the following args
*  Usage:
        Vehicle_Detector.py [-v] <INPUT_PATH> <OUTPUT_PATH>

    Options:

    -h --help                               show this screen
    -v                                 process video file instead of image
                
    Ex: for single image input
    >> python Vehicle_Detector.py C:/test.jpg D:/out.jpg


    Ex: for video input
    >> python Vehicle_Detector.py -v C:/test.mp4 D:/out.mp4  
