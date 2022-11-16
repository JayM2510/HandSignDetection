import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # For webcam
detector = HandDetector(maxHands=1)  # Detecting number of hands

offset = 20
imgSize = 300

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        imgCrop = img[y - offset: y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        imgWhite[0: imgCropShape[0], 0: imgCropShape[1]] = imgCrop

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
