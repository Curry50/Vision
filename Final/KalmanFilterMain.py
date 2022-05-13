import serial
import cv2
from Runes_detector import Runes_detector
from kalmanfilter import KalmanFilter
from SerialCommunication import SerialCommunication
from VideoCapture import VideoCapture


vc = VideoCapture()
od = Runes_detector()
sc = SerialCommunication()
kf = KalmanFilter()

cap = vc.Capture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(15,-20)
try:
    ser = serial.Serial("/dev/ttyUSB0",115200,timeout = 0.01)
except:
    pass

while True:
    ret, frame = vc.CaptureRead(cap)
    frame = cv2.resize(frame,None,fx=1/5,fy=16/45)
    if ret is False:
        break
    green_bbox = od.detect(frame)
    data_x = []
    data_y = []
    data_x2 = []
    data_y2 = []
    for i in range(len(green_bbox)):
        x,y,x2,y2 = green_bbox[i]
        data_x.append(x)
        data_y.append(y)
        data_x2.append(x2)
        data_y2.append(y2)
        cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 4)
    
    try:
        Xcenter = int((data_x[0] + data_x[1])/2)
        Ycenter = int((data_y[0]-(data_y[0]-data_y2[0])/2 + data_y[1]-(data_y[1]-data_y2[1])/2 )/2)
        predicted = kf.predict(Xcenter,Ycenter)
        cv2.circle(frame,(Xcenter,Ycenter),10,(0,0,255),-1)
        cv2.circle(frame,(predicted[0],predicted[1]),10,(255,0,0),-1)
        sc.dataProcess(ser,predicted[0],predicted[1])
    except:
        print("No Armor")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break