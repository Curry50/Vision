import serial
import cv2
from Runes_detector import Runes_detector
from kalmanfilter import KalmanFilter
from SerialCommunication import SerialCommunication
from VideoCapture import VideoCapture

#initialization
vc = VideoCapture()
od = Runes_detector()
sc = SerialCommunication()
kf = KalmanFilter()
ser = serial.Serial("COM5",115200,timeout = 0.01)
cap = vc.Capture(1)
#set parameters
cap.set(3,1280)
cap.set(4,720)
cap.set(15,-9)



#main loop
while True:
    ret, frame = vc.CaptureRead(cap)
    frame = cv2.resize(frame,None,fx=1/5,fy=16/45)
    if ret is False:
        break

    green_bbox = od.detect(frame)
    x, y, x2, y2 = green_bbox
    #sc.dataProcess(ser,x,y)
    #sc.sendData(ser,[abs(x),abs(y)],3)
    predicted1 = kf.predict(x,y)
    sc.dataProcess(ser,predicted1[0] , predicted1[1])
    cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 4)#红色实际框
    cv2.rectangle(frame,(predicted1[0],predicted1[1]),(x2+predicted1[0]-x ,y2-y+predicted1[1]),(255,0,0),4)#蓝色预测框
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)#150
    if key == 27:
        break