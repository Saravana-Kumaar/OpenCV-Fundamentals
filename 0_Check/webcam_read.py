import cv2

# to read a video , frame by frame

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Video Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

'''
to set width , heigth and brightness

cap.set(3 , h)
cap.set(4 , w)
cap.set(10 , b)

'''