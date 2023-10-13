import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread("../sample_images/person.jpeg")
cv2.imshow("No detection" , image)

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray , 1.1 , 4)

for x,y,w,h in face:
    cv2.rectangle(image , (x , y) , (x+w , y+h) , (213,143,67) , 4)



cv2.imshow("With detection" , image)

cv2.waitKey(5000)
cv2.destroyAllWindows()