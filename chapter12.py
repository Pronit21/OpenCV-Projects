import cv2

# Load the cascade
eyeCascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

# Read the image
img = cv2.imread('Resources/lena.png')

# Convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect eyes
eyes = eyeCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

# Draw rectangles around the eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the result
cv2.imshow("Result", img)
cv2.waitKey(0)
