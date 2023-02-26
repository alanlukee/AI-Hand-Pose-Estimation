import mediapipe as mp
import cv2 as cv
import numpy as np
import uuid   #unique unifrom identifier
import os 


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        isTrue,frame = cap.read()

        


        frame.flags.writeable= False

        #detections

        results=hands.process(frame)


        frame.flags.writeable = True
        #image = cv.cvtColor(frame,cv.COLOR_RGB2BGR)


        print(results.multi_hand_landmarks)
        if(results.multi_hand_landmarks):
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

        #save our image
        #v.imwrite(os.path.join('Output Images', '{}.jpg'.format(uuid.uuid1())),frame)
        cv.imshow("Hand Tracking",frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    cap.release()
    cv.destroyAllWindows()
    print(results.multi_hand_landmarks)
    
