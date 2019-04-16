import cv2 as cv

img = cv.imread('./testImages/RAD_BEDOUR_20190413_0100_BEGRIM_SYS001.png', 0)
cv.imshow('testing', img)
cv.waitKey(0)
cv.destroyAllWindows()
