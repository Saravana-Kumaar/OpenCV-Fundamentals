import cv2

# to read a video , frame by frame

cap = cv2.VideoCapture('../sample_images/auto.gif')

print("Enter the frame delay :")
delay = int(input())
'''
1 -> 1ms between frame to frame
1000 -> 1second 
0 -> space to read the seqential frames
'''

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Video Frame', frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
