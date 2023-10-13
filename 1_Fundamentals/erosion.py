# erosion decreases the thickness of the edgs

# identify the edges and erode it (if the edges are too large)

import cv2
import numpy as np

# create a kernel for dilation (hint:odd number matrics[for sliding window operation])

kernel = np.ones((5,5) , np.uint8)

image = cv2.imread("../sample_images/mycar.jpeg")

# threshold definitions 
low_thresh = 400
high_thresh = 500

# first identify the edges 
edge = cv2.Canny(image, low_thresh, high_thresh)

# dilated 
dil_image = cv2.dilate(edge , kernel , iterations=1)

# erode the dilated
erode_image = cv2.erode(dil_image , kernel , iterations=1)


cv2.imshow("Original", image)
cv2.imshow("Edged image", edge)
cv2.imshow("Dilated image", dil_image)
cv2.imshow("Eroded", erode_image)

cv2.waitKey(0)