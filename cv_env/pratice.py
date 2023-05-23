import cv2 
import numpy as np 

src = cv2.imread('imgs/little.jpg')
dsd = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)

src_hsv = cv2.cvtColor(dsd, cv2.COLOR_BGR2HSV)
def trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')
    smin = cv2.getTrackbarPos('S_min', 'dst')
    smax = cv2.getTrackbarPos('S_max', 'dst')
    vmin = cv2.getTrackbarPos('V_min', 'dst')
    vmax = cv2.getTrackbarPos('V_max', 'dst')

    dst = cv2.inRange(dsd, (hmin, smin, vmin), (hmax, smax, vmax))
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')


cv2.createTrackbar('H_min', 'dst', 0, 179, trackbar)
cv2.createTrackbar('H_max', 'dst', 50, 179, trackbar)

cv2.createTrackbar('S_min', 'dst', 0, 255, trackbar)
cv2.createTrackbar('S_max', 'dst', 100, 255, trackbar)

cv2.createTrackbar('V_min', 'dst', 0, 255, trackbar)
cv2.createTrackbar('V_max', 'dst', 100, 255, trackbar)


trackbar(0)

cv2.waitKey(0)
cv2.destroyAllWindows()


