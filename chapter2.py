import cv2

cap = cv2.VideoCapture("Resources/bird.mp4")
paused = False

while True:
    if not paused:
        success, img = cap.read()
        if not success:
            break
        cv2.imshow("Video", img)
    
    key = cv2.waitKey(1)
    
    if key & 0xFF == ord('q'):
        break
    elif key == ord(' '):  # Toggle play/pause on spacebar press
        paused = not paused

cap.release()
cv2.destroyAllWindows(0)
