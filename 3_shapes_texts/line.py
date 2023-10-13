import cv2
import numpy as np

image_2 = np.zeros((600,800 , 3))

image_2[:] = (0 , 255 , 0 )


# draw a line 
cv2.line(image_2 , (0,0) , (800 ,600) , (255,0,0) , 3 )
# syntax -> (image , start point , end point  , colour , pixel , size)

cv2.line(image_2 , (0,600) , (800,0) , (0,0,255) , 3 )

cv2.line(image_2 , (0,300 ) , (800 ,300) , (255,255,255) , 3 )

cv2.imshow("green channel" , image_2)

print(image_2.shape)

cv2.waitKey(3000)
cv2.destroyAllWindows()