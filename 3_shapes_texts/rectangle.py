import cv2
import numpy as np

image_2 = np.zeros((600,800 , 3))

image_2[:] = (0 , 255 , 0 )


cv2.rectangle(image_2 , (0,0) , (400 , 300) , (0 , 0 , 255) , 3)
cv2.rectangle(image_2 , (200 , 150), (500,400) , (255 , 0, 0) , cv2.FILLED)


cv2.imshow("green channel" , image_2)

print(image_2.shape)

cv2.waitKey(3000)
cv2.destroyAllWindows()