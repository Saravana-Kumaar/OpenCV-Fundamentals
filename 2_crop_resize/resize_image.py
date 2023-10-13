import cv2

image = cv2.imread("../sample_images/mycar.jpeg")

resize = cv2.resize(image , (1000 , 600 ))

cv2.imshow("Original" , image)
cv2.imshow("Resized" , resize)

print("original size : " , image.shape)
print("resized size : " , resize.shape)


cv2.waitKey(5000)
cv2.destroyAllWindows()

# dimensions -> (height , width , colour channels)