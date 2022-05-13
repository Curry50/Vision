import cv2
import numpy as np


class Runes_detector:
    def __init__(self):
        self.low_green = np.array([35, 43, 46])
        self.high_green = np.array([77, 255, 255])
        self.low_blue = np.array([100, 43, 46])
        self.high_blue = np.array([124, 255, 255])
    def detect(self, frame):
        data = []
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        k = np.ones((11,11),np.uint8)
        mask = cv2.inRange(hsv_img, self.low_blue, self.high_blue)
        mask = cv2.erode(mask,k)
        mask = cv2.dilate(mask,k)
        cv2.imshow("mask",mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for i in range(len(contours)):  
            x, y, w, h = cv2.boundingRect(contours[i]) 
            aspectRatio = float(w) / h  # 宽高比
            if cv2.contourArea(contours[i]) > 0 and aspectRatio < 1:
                #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 画出矩形
                #print(int(15 * 95 / w))
                cv2.putText(frame, "Distance " + str(int(35 * 225 / w))+"cm", (100, 200), cv2.FONT_HERSHEY_TRIPLEX, 1,
                            (0, 255, 0))
                x, y, w, h = cv2.boundingRect(contours[i])
                box = [x,y,x+w,y+h]
                if(len(data) < 2):
                    data.append(box)
                
                
        return data
