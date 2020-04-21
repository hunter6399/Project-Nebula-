import cv2
vidcap = cv2.VideoCapture('output.mov')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 5
success = getFrame(sec)
while success:
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
