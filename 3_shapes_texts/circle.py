import cv2
import numpy as np

image_2 = np.zeros((600,800 , 3))

image_2[:] = (0 , 255 , 0 )


cv2.circle(image_2 , (400 , 300) , 200 , (255,0,0) , 4)
cv2.circle(image_2 , (400 , 300) , 100 , (0,0,255) , -1)


cv2.imshow("green channel" , image_2)

print(image_2.shape)

cv2.waitKey(3000)
cv2.destroyAllWindows()