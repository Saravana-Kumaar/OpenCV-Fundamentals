# using gaussian blur function
import cv2

image = cv2.imread("../sample_images/mycar.jpeg")

kernal_size_1 = (1, 1)
kernal_size_2 = (3, 3)
kernal_size_3 = (7, 7)

# we could specify the size of the kernel
# it can be any old values for kernel

blurred_image_one = cv2.GaussianBlur(image, kernal_size_1, 0)
blurred_image_two = cv2.GaussianBlur(image, kernal_size_2, 0)
blurred_image_three = cv2.GaussianBlur(image, kernal_size_3, 0)


cv2.imshow('Original Image', image)
cv2.imshow('gaussian blur with (1,1)', blurred_image_one)
cv2.imshow('gaussian blur with (3,3)', blurred_image_two)
cv2.imshow('gaussian blur with (7,7)', blurred_image_three)


cv2.waitKey(0)
