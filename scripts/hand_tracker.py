import cv2 
import mediapipe as mp
import time
import keyboard
cap = cv2.VideoCapture(0)


mphands = mp.solutions.hands
hands = mphands.Hands()
draw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success, image = cap.read()
    flipped = cv2.flip(image,1)
    imgRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for lms in results.multi_hand_landmarks:
            draw.draw_landmarks(flipped, lms, mphands.HAND_CONNECTIONS)
    cTime = time.time()
    FPS = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(flipped, str(int(FPS)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow('Sexe_webcam',flipped)
    
    
    # print(results.multi_hand_landmarks)
    cv2.waitKey(100)

  


