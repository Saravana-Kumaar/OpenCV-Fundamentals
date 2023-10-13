import cv2
import numpy as np

# grayscale image of 400 x 400 size
image_1 = np.zeros((600,800))

# with 3 colour channels
image_2 = np.zeros((600,800 , 3))


cv2.imshow("The gray scale with single channel" , image_1)
cv2.imshow("The gray scale with three channel" , image_2)


cv2.waitKey(2000)
cv2.destroyAllWindows()

# blue channel
image_2[:] = (255 , 0 , 0 )
cv2.imshow("Blue channel" , image_2)

# green channel
image_2[:] = (0 , 255 , 0 )
cv2.imshow("green channel" , image_2)

# red channel
image_2[:] = ( 0 , 0 , 255 )
cv2.imshow("red channel" , image_2)

cv2.waitKey(2000)
cv2.destroyAllWindows()


image_1 = np.ones((600,800))
cv2.imshow("just white with 3 channels" , image_1)


cv2.waitKey(2000)
cv2.destroyAllWindows()