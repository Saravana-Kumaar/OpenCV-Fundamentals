'''
Contour detection or extraction is a fundamental image processing 
technique used to identify and locate the boundaries
of objects within digital images
'''

# work flow
# image -> gray scale -> find edges -> find contours -> draw contours

import cv2

image = cv2.imread("../sample_images/shape.png")


# step 1 (convert into gray scale)
greyscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)


# step 2 (find edges using canny edge detector)
lower_threshold = 100
higher_threshold = 150

edged_image = cv2.Canny(greyscale_image.copy() , lower_threshold , higher_threshold)

# step 3 (find the contour now)

detected_contour , hirearchy = cv2.findContours(edged_image , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

# step 4 (find the length of the contour)
print(f"The length of the contour {len(detected_contour)}")

# step 5 (draw contours)
image_copy = image.copy()
cv2.drawContours(image_copy , detected_contour , -1 ,(0 , 0 , 255) , 3)


cv2.imshow("Original Image", image)
cv2.imshow("gray scale" , greyscale_image)
cv2.imshow("edged image" , edged_image)
cv2.imshow("contour image" , image_copy)

print(f"The length of the contour {len(detected_contour)}")
cv2.waitKey(5000)
cv2.destroyAllWindows()