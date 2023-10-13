# using canny edge detector
import cv2

image = cv2.imread("../sample_images/mycar.jpeg")

# setting the threshold values
low_thresh_1 = 100
high_thresh_1 = 120

low_thresh_2 = 400
high_thresh_2 = 500

# apply canny edge detection with defined threaholds
edge1 = cv2.Canny(image, low_thresh_1, high_thresh_1)
edge2 = cv2.Canny(image, low_thresh_2, high_thresh_2)


cv2.imshow("Original", image)
cv2.imshow("Edges", edge1)
cv2.imshow("Edges", edge2)


cv2.waitKey(0)
