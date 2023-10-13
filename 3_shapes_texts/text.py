import cv2
import numpy as np

image_2 = np.zeros((600,800 , 3))

image_2[:] = (0 , 255 , 0 )


cv2.putText(image_2 , "Hello World" , (150 , 200) , cv2.FONT_HERSHEY_COMPLEX  , 3 , (255 , 0 , 0 ) , 7)
cv2.putText(image_2 , "Open CV" , (200 , 300) , cv2.FONT_ITALIC  , 3 , (255 , 0 , 255 ) , 7)


cv2.imshow("green channel" , image_2)

print(image_2.shape)

cv2.waitKey(3000)
cv2.destroyAllWindows()