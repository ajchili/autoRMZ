import cv2
import numpy as np
import statistics
import os

image_width = 1024
image_height = 755
graph_offset = 64
graph_inset = 96


def map_likely_meteor_to_object(element):
    return {
        'start': {
            'x': element[0],
            'y': element[1]
        },
        'end': {
            'x': element[2],
            'y': element[3]
        }
    }


def analyze_image(path):
    # Pull image from file
    img = cv2.imread(path)

    # Crops image to remove border
    crop = img[graph_offset:-graph_inset, graph_offset:-graph_inset]

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

    likely_meteors = []
    likely_baseline = 0
    likely_meteor_distances = []

    # Get lines from edges
    lines = cv2.HoughLinesP(merge, 1, np.pi, 1, minLineLength=50)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                likely_meteors.append((x1, y1, x2, y2))
    lines = cv2.HoughLinesP(horizontal_merge, 1, np.pi / 180, 1, minLineLength=50)
    if lines is not None:
        y = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                y.append(y1)
        likely_baseline = statistics.mean(y) + 64

    # Draw likely baseline
    cv2.line(img, (graph_offset, likely_baseline), (image_width - graph_inset, likely_baseline), (255, 255, 255), 2)

    # Draw likely meteors
    for i, (x1, y1, x2, y2) in enumerate(likely_meteors):
        middle = statistics.mean([y1, y2]) + 64
        distance = max(min(abs(likely_baseline - middle), 255), 0)
        distance_int = np.int16(distance).item()
        likely_meteor_distances.append(abs(likely_baseline - middle))
        cv2.rectangle(img, (x1 + graph_offset, y1 + graph_offset), (x2 + graph_offset, y2 + graph_offset),
                      (0, 255 - distance_int, distance_int), 2)

    if len(likely_meteor_distances) > 0:
        average_likely_meteor_distance = statistics.mean(likely_meteor_distances)
        if average_likely_meteor_distance > 50:
            cv2.putText(img,
                        'Incorrect baseline detected! (Average distance of {})'.format(
                            average_likely_meteor_distance),
                        (64, 48), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1,
                        cv2.LINE_AA)
    else:
        cv2.putText(img,
                    'No likely meteors detected!',
                    (64, 48), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1,
                    cv2.LINE_AA)

    # Show original image with data overlay
    cv2.imshow('output'.format(path), img)
    cv2.waitKey(0)

    # Returns parsed data
    return {
        'likelyMeteors': list(map(map_likely_meteor_to_object, likely_meteors)),
        'likelyBaseline': likely_baseline,
        'imageName': path
    }


for file_name in os.listdir('./dataset/test_set'):
    if file_name != '.gitkeep':
        path = os.path.join('./dataset/test_set', file_name)
        if os.path.isfile(path):
            # TODO: Determine what to do with data
            data = analyze_image(path)
