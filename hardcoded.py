import cv2
import numpy as np
import statistics
import os


def analyze_image(path):
    # Pull image from file
    img = cv2.imread(path)

    # Crops image to remove border
    crop = img[64:-96, 64:-96]

    # Convert to greyscale
    gray = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)

    # Blur image to remove hard edges
    blur = cv2.blur(gray, (4, 30))
    horizontal_blur = cv2.blur(gray, (30, 4))

    # Get edges in image
    edges = cv2.Canny(blur, 50, 150)
    horizontal_edges = cv2.Canny(horizontal_blur, 50, 150)

    # Fill edges
    merge = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    horizontal_merge = cv2.morphologyEx(horizontal_edges, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))

    # Get lines from edges
    lines = cv2.HoughLinesP(merge, 1, np.pi, 1, minLineLength=50)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(img, (x1 + 64, y1 + 64), (x2 + 64, y2 + 64), (255, 105, 255), 2)
    lines = cv2.HoughLinesP(horizontal_merge, 1, np.pi / 180, 1, minLineLength=50)
    if lines is not None:
        y = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                y.append(y1)
        mean = statistics.mean(y) + 64
        cv2.line(img, (64, mean), (928, mean), (255, 255, 255), 2)

    # Show image
    cv2.imshow('output', img)
    cv2.waitKey(0)


for file_name in os.listdir('./dataset/test_set'):
    if file_name != '.gitkeep':
        path = os.path.join('./dataset/test_set', file_name)
        if os.path.isfile(path):
            analyze_image(path)
