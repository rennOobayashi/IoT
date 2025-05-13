#only one time
import cv2
import time

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cam.isOpened():
    print('Cam isnt opened!')
    exit()

ret, img = cam.read()

if not ret:
    print('Frame read error!')
    exit()

cv2.imshow('CAM', img)
time.sleep(1)
cv2.imread('cam.jpg', img)
cam.relaese()
cv2.destroyAllWindows()

