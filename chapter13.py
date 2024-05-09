import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('Resources/two.jpg')

for barcode in decode(img):
    print(barcode.data)