import cv2

# Load the cascade classifier for pedestrians
pedestrianCascade = cv2.CascadeClassifier("haarcascades/haarcascade_fullbody.xml")

# Read the image
img = cv2.imread('Resources/street.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect pedestrians in the image
pedestrians = pedestrianCascade.detectMultiScale(imgGray, 1.1, 4)

# Draw rectangles around the detected pedestrians
for (x, y, w, h) in pedestrians:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)

# Display the result
cv2.imshow("Result", img)
cv2.waitKey(0)
