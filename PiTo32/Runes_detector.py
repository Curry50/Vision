import cv2
import numpy as np


class Runes_detector:
    def __init__(self):
        # Create mask for orange color
        self.low_green = np.array([35, 43, 46])
        self.high_green = np.array([77, 255, 255])

    def detect(self, frame):
        k = np.ones((9,9),np.uint8)
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks with color ranges
        mask = cv2.inRange(hsv_img, self.low_green, self.high_green)
        mask = cv2.erode(mask,k)
        mask = cv2.dilate(mask,k)
        cv2.imshow("mask",mask)
        # Find Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        box = (0, 0, 0, 0)
        for i in range(len(contours)):  # 循环
            x, y, w, h = cv2.boundingRect(contours[i])  # 矩形的包围框
            aspectRatio = float(w) / h  # 宽高比
            #if aspectRatio < 1.4 / 0.9:  # 宽高比
                #if aspectRatio > 1:
            if cv2.contourArea(contours[i]) > 200:
                cv2.putText(frame, "Distance " + str(int(35 * 225 / w))+"cm", (100, 200), cv2.FONT_HERSHEY_TRIPLEX, 1,
                            (0, 255, 0))
                x, y, w, h = cv2.boundingRect(contours[i])
                box = (x, y, x + w, y + h)
                break


        return box