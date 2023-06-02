import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detecter = HandDetector(maxHands=2)
while True:
    success, img = cap.read()
    img = cv2.flip(img,1) 
    hands, img = detecter.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        imgCrop = img[y:y + h, x:x + w]
        cv2.imshow("ImageCrop", imgCrop)
    cv2.imshow("zurag",img)
    cv2.waitKey(1)