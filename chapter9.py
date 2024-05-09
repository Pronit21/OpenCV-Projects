import cv2
import numpy as np

def empty(a):
    pass

# Function to stack multiple images horizontally or vertically
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # Resize images to ensure they have the same dimensions
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # Convert grayscale images to BGR format
                if len(imgArray[x][y].shape) == 2: 
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create blank image for stacking
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        # Stack images horizontally
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack rows vertically
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

# Path to the image
path = 'Resources/lambo.png'

# Create a window for trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

# Create trackbars for adjusting HSV values
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    # Read the image
    img = cv2.imread(path)
    # Convert image to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Get current trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    # Define lower and upper bounds for mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Create mask using inRange function
    mask = cv2.inRange(imgHSV, lower, upper)
    # Apply bitwise AND operation to original image and mask
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Stack images for display
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    # Display the stacked images
    cv2.imshow("Stacked Images", imgStack)

    # Wait for key press
    cv2.waitKey(1)
