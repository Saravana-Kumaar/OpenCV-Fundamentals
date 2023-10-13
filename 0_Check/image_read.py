import cv2

image = cv2.imread("../sample_images/mycar.jpeg")

cv2.imshow('Original Image', image)

cv2.waitKey(0) #will add infinite delay
# cv2.waitKey(5000) #will add 5s delay
