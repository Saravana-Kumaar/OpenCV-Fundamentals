import cv2
# 97 179 64 255 85 255 -> we got this from the last colour1.py program after selecting the detected part into white

image = cv2.imread("../sample_images/mycar.jpeg")

imgHSV = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)


lower_range=(97,64,85)
upper_range=(179,255,255)

mask=cv2.inRange(imgHSV , lower_range , upper_range)

color_image = cv2.bitwise_and(image , image , mask=mask)

cv2.imshow("detected colour" , color_image)

cv2.waitKey(10000)
cv2.destroyAllWindows()

