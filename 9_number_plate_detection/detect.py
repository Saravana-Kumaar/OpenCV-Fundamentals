import cv2

cap = cv2.VideoCapture("../sample_images/sample_vid.mp4")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_russian_plate_number.xml")

while True:
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

        bounding_box = face_cascade.detectMultiScale(gray , 1.1, 1)

        for x , y , w , h in bounding_box:
            cv2.rectangle(frame , (x , y) , (x + w , y + h) , (255, 255 , 255) , 3)

        cv2.imshow('Video Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()