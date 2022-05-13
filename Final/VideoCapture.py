import cv2

class VideoCapture:
    def Capture(self,CameraIndex):
        cap =cv2.VideoCapture(CameraIndex)
        return cap
    
    def CaptureSet(self,Cap,Index,Size):
        Cap.set(Index,Size)
        
    def CaptureRead(self,Cap):
        ret,frame = Cap.read()
        return ret,frame