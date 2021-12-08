import cv2
import numpy as np
import fileinput as fi

frozenModel = './model/frozen_inference_graph.pb'
configFile  = './model/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
classNames  = []
model = None


videoCapture = None

def startCamera():
    global videoCapture
    videoCapture = cv2.VideoCapture(1) # NOTE: Make sure to pass the correct ID of your device. If you only have one Webcam attached then this is ID is 0.

def stopCamera():
    videoCapture.release()

def loadClassnames():
    global classNames
    with fi.input( ('./model/coco.names') ) as f:
        for line in f:
            classNames.append(line.strip('\n'))

def setupModel():
    global model
    model = cv2.dnn_DetectionModel(frozenModel, configFile)
    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

def recognize():
    results = []
    ret, frame = videoCapture.read()
    smallFrame = frame # cv2.resize(frame, (0, 0), fx=1.0, fy=1.0)

    classIDs, confidences, bboxArray = model.detect(smallFrame, confThreshold=0.6, nmsThreshold=0.1)

    for classID, confidence, bbox in zip(classIDs, confidences, bboxArray):
        if confidence > 0.4:
            results.append(classNames[classID - 1]) # classID starts at 1
    
    return results



