
import cv2
import numpy as np

image = cv2.imread("../sample_images/mycar.jpeg")

kernal_size = (3, 3)
blurred_image = cv2.GaussianBlur(image, kernal_size, 0)

image_horizontal_stack = np.vstack((image , blurred_image))

cv2.imshow("Vertical Join"  , image_horizontal_stack)


cv2.waitKey(5000)
cv2.destroyAllWindows()