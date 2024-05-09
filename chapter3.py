import cv2

# Define the desired frame width and height
frameWidth = 480
frameHeight = 640

# Initialize the video capture object for webcam (0 indicates the default webcam)
cap = cv2.VideoCapture(0)

# Set the frame width and height of the captured video
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Set the brightness (ID 10 for brightness) of the webcam to 20
cap.set(10, 20)

# Infinite loop to continuously capture frames from the webcam
while True:
    # Read a frame from the webcam
    success, img = cap.read()
    
    # Display the captured frame
    cv2.imshow("Result", img)
    
    # Check if the user pressed the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Exit the loop if 'q' is pressed

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
