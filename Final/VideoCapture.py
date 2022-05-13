#导入相关模块
import cv2

#定义VideoCapture类
class VideoCapture:
    #捕捉画面
    def Capture(self,CameraIndex):
        cap =cv2.VideoCapture(CameraIndex)
        return cap
    
    #设置画面相关参数
    def CaptureSet(self,Cap,Index,Size):
        Cap.set(Index,Size)
    
    #读取画面
    def CaptureRead(self,Cap):
        ret,frame = Cap.read()
        return ret,frame
