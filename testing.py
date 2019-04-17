import numpy as np
import cv2

img = cv2.imread('./dataset/test_set/RAD_BEDOUR_20190413_0100_BEGRIM_SYS001.png', 0)
edges = cv2.Canny(img,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180, 200)
# blur = cv2.GaussianBlur(img, (15, 15), 0)
# lines = cv2.HoughLinesP(blur, 1, np.pi / 180, 50, None, 50, 300)
print(lines)
cv2.imshow('testing', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
