# consider i am going to join the original and the blurred right after it 

import cv2
import numpy as np

image = cv2.imread("../sample_images/mycar.jpeg")

kernal_size = (3, 3)
blurred_image = cv2.GaussianBlur(image, kernal_size, 0)

image_horizontal_stack = np.hstack((image , blurred_image))

cv2.imshow("Horizontal Join"  , image_horizontal_stack)


cv2.waitKey(5000)
cv2.destroyAllWindows()

'''
if there is any resizing issue 
use 
cv2.resize(image , (w , h))
'''