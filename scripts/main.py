import cv2 
import mediapipe as mp
import time
import keyboard
cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
draw = mp.solutions.drawing_utils
while True:
    success, image = cap.read()
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for lms in results.multi_hand_landmarks:
            draw.draw_landmarks(image, lms, mphands.HAND_CONNECTIONS)
    cv2.imshow('Sexe_webcam',image)
    
    
    print(results.multi_hand_landmarks)
    cv2.waitKey(100)
  


