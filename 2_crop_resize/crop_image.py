# images -> 2 dimensional array 
# just slice it
import cv2

image = cv2.imread("../sample_images/mycar.jpeg")

# crop by half in width and height

h = int(image.shape[0]/2)
w = int(image.shape[1]/2)
print(h , w)
crop_image_1 = image[0:h , 0:w ]

cv2.imshow("Original" , image)
cv2.imshow("crop image" , crop_image_1)

print("original size : " , image.shape)
print("cropped size : " , crop_image_1.shape)


cv2.waitKey(5000)
cv2.destroyAllWindows()