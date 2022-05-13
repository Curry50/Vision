#导入相关模块
import serial
import cv2
from Runes_detector import Runes_detector
from kalmanfilter import KalmanFilter
from SerialCommunication import SerialCommunication
from VideoCapture import VideoCapture

#初始化
vc = VideoCapture()
od = Runes_detector()
sc = SerialCommunication()
kf = KalmanFilter()

#设置画面相关参数
cap = vc.Capture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(15,-20)

#串口初始化
try:
    ser = serial.Serial("/dev/ttyUSB0",115200,timeout = 0.01)
except:
    pass

#主循环
while True:
    ret, frame = vc.CaptureRead(cap) #读取画面
    frame = cv2.resize(frame,None,fx=1/5,fy=16/45) #将图像的分辨率缩放至256*256，便于通信传输数据
    if ret is False:
        break
    green_bbox = od.detect(frame) #获取检测到的矩形包围框的x,y,w,h信息
    
    #建立列表，储存检测到的装甲板的两个有色灯条的x,y,w,h信息
    data_x = [] 
    data_y = []
    data_x2 = []
    data_y2 = []
    
    #遍历两个有色灯条的x,y,w,h信息
    for i in range(len(green_bbox)):
        x,y,x2,y2 = green_bbox[i]
        data_x.append(x)
        data_y.append(y)
        data_x2.append(x2)
        data_y2.append(y2)
        cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 4) #绘出灯条的红色矩形包围框
    
    try:
        Xcenter = int((data_x[0] + data_x[1])/2) #求取装甲板中心横坐标
        Ycenter = int((data_y[0]-(data_y[0]-data_y2[0])/2 + data_y[1]-(data_y[1]-data_y2[1])/2 )/2) #求取装甲板中心纵坐标
        predicted = kf.predict(Xcenter,Ycenter) #利用卡尔曼滤波预测中心坐标
        cv2.circle(frame,(Xcenter,Ycenter),10,(0,0,255),-1) #绘出红色实际中心点
        cv2.circle(frame,(predicted[0],predicted[1]),10,(255,0,0),-1) #绘出蓝色预测中心点
        sc.dataProcess(ser,predicted[0],predicted[1]) #处理预测数据并向stm32发送预测中心点坐标
    except:
        print("No Armor")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
