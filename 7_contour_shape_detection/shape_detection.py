import cv2

image = cv2.imread("../sample_images/test2.jpg")
greyscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
lower_threshold = 100
higher_threshold = 150
edged_image = cv2.Canny(greyscale_image.copy() , lower_threshold , higher_threshold)
detected_contour , hirearchy = cv2.findContours(edged_image , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)


# to find the shape

# step 1 (iterate the contours)
image_copy = image.copy()
for i in detected_contour:

    # step 2 (find the area)
    area = cv2.contourArea(i)
    print("area" , area)

    #step 3 (find the arc length of the contours)
    peri = cv2.arcLength(i , True)

    #step 4 (find the conner points in the each of the shape)
    approx = cv2.approxPolyDP(i , 0.02*peri , True)

    # step 5 (no of the conner points )
    print("No of the conner points " , len(approx))

    objectCornerpoints =  len(approx)

    # step 6 (draw bounding box)
    x,y,w,h = cv2.boundingRect(approx)

    cv2.rectangle(image_copy,(x , y) , (x + w , y + h) , (0 , 0 , 255) , 3)

    if objectCornerpoints == 3:
        object_type = "Triangle"
    elif objectCornerpoints == 4:
        ar = w/float(h)
        if ar > 0.98 and ar < 1.03:
            object_type = "Square"
        else:
            object_type = "Rectangle"
    elif objectCornerpoints > 4:
        object_type = "Circle"
    else:
        object_type = None

    cv2.putText(image_copy , object_type , (x+(w//2)-25 , y+(h//2)-25) , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (255 , 144 , 0) , 2)
 

cv2.imshow("Original Image", image)
cv2.imshow("Shape detected" , image_copy)
cv2.waitKey(5000)
cv2.destroyAllWindows()