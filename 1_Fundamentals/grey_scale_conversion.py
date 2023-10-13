import cv2

image = cv2.imread("../sample_images/mycar.jpeg")

grey_version = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow('Original Image', image)
cv2.imshow('Gray Scaled Image', grey_version)

cv2.waitKey(0)
