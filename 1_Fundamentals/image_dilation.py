# dilation is used to increase the thickness of the edges

# identify the edges and dilate it

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

# dilated image
dil_image = cv2.dilate(edge , kernel , iterations=1)


cv2.imshow("Original", image)
cv2.imshow("Edged image", edge)
cv2.imshow("Dilated", dil_image)


cv2.waitKey(0)
