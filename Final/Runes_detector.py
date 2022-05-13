导入相关模块
import cv2
import numpy as np

#定义Runes_detector类
class Runes_detector:
    def __init__(self):
        #定义HSV通道下的颜色阈值上限和下限
        self.low_green = np.array([35, 43, 46])
        self.high_green = np.array([77, 255, 255])
        self.low_blue = np.array([100, 43, 46])
        self.high_blue = np.array([124, 255, 255])
        
    def detect(self, frame):
        data = []
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #从BGR颜色空间转换到HSV颜色空间
        k = np.ones((5,5),np.uint8) #定义卷积核
        mask = cv2.inRange(hsv_img, self.low_blue, self.high_blue) #二值化
        mask = cv2.erode(mask,k) #腐蚀操作
        mask = cv2.dilate(mask,k) #膨胀操作
        cv2.imshow("mask",mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #寻找轮廓并保存轮廓信息
        
        #遍历所有轮廓
        for i in range(len(contours)):  
            x, y, w, h = cv2.boundingRect(contours[i]) #返回矩形包围框的坐标信息
            aspectRatio = float(w) / h  #宽高比
            if 0.6 < cv2.contourArea(contours[i])/(w*h) and 1/2 >= aspectRatio and cv2.contourArea(contours[i]) > 0: #利用轮廓面积、宽高比和轮廓面积与矩形包围框面积之比筛选出目标轮廓
                #cv2.putText(frame, "Distance " + str(int(35 * 225 / w))+"cm", (100, 200), cv2.FONT_HERSHEY_TRIPLEX, 1,
                #            (0, 255, 0)) #测定距离
                x, y, w, h = cv2.boundingRect(contours[i]) #得到目标矩形包围框的坐标信息
                box = [x,y,x+w,y+h] #保存矩形包围框的坐标信息
                if(len(data) < 2): #设定条件，始终只检测到两个灯条
                    data.append(box)
                
                
        return data #返回目标轮廓坐标信息
