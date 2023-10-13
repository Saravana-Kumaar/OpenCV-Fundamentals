# wrap is like selecting a part from image and flatting it 
import cv2
import numpy as np

image = cv2.imread("../sample_images/joker.jpeg")
cv2.imshow("Just going to select the joker from this image" , image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

width = 400
height = 500

position1 = np.float32([[491,184] , [663,267]  , [348,449] , [524,542]])

position2 = np.float32([[0,0] , [width , 0 ] , [ 0 , height] , [width , height]])

matrics = cv2.getPerspectiveTransform(position1 , position2)

output_image = cv2.warpPerspective(image , matrics , (width , height))



cv2.imshow("Original image" , image)
cv2.imshow('Wrapped Image', output_image)


cv2.waitKey(10000) 
cv2.destroyAllWindows()