# after the output -> try the make the colour region into white inrder to detect it
import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars" , 640 , 240)

cv2.createTrackbar("Hue Min" , "TrackBars" , 0 , 179  , empty)
cv2.createTrackbar("Hue Max" , "TrackBars" , 179 , 179 , empty)
cv2.createTrackbar("Sat Min" , "TrackBars" , 0 , 255 , empty)
cv2.createTrackbar("Sat Max" , "TrackBars" , 255 , 255 , empty)
cv2.createTrackbar("Val Min" , "TrackBars" , 0 , 255 , empty)
cv2.createTrackbar("Val Max" , "TrackBars" , 255 , 255 , empty)

while True:
    image = cv2.imread("../sample_images/mycar.jpeg")

    imgHSV = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min" , "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max" , "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min" , "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max" , "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min" , "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max" , "TrackBars")


    print(h_min , h_max , s_min , s_max , v_min , v_max)

    lower=np.array([h_min , s_min , v_min ])
    upper=np.array([h_max , s_max ,  v_max])

    mask = cv2.inRange(imgHSV , lower , upper)

    cv2.imshow("Original" , image)

    cv2.imshow("HSV image" , imgHSV)

    cv2.imshow("mask" , mask)

    cv2.waitKey(1)



cv2.waitKey(2000)
cv2.destroyAllWindows()