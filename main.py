print("hello hand mouse!")
from turtle import distance
import cv2
import mediapipe as mp
import pyautogui    
import numpy as np
import time
import math
import threading
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
last_time = 0

with mp_hands.Hands(max_num_hands=1) as hands:
    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        if result.multi_hand_landmarks:
            #print("HAND DETECTED")

            for handLms in result.multi_hand_landmarks:
                #print(handLms)
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                for id, lm in enumerate(handLms.landmark):              
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    #print(id, cx, cy)
                    if id == 8:
                        cv2.circle(img=frame, center=(cx, cy), radius=15, color=(255, 255, 255), thickness=cv2.FILLED)    
                        index_x = int(handLms.landmark[8].x * w)
                        index_y = int(handLms.landmark[8].y * h)
                        mouse_x = np.interp(index_x, [0, w], [0, pyautogui.size().width])
                        mouse_y = np.interp(index_y, [0, h], [0, pyautogui.size().height])
                        pyautogui.moveTo(mouse_x, mouse_y)  
                    if id==4:
                        thumb_x=int(handLms.landmark[4].x * w)
                        thumb_y=int(handLms.landmark[4].y * h)
                    if id==12:
                        middle_x=int(handLms.landmark[12].x * w)
                        middle_y=int(handLms.landmark[12].y * h)
                distance_index_thumb=math.hypot(thumb_x - index_x, thumb_y - index_y)
                distance_middle_thumb=math.hypot(middle_x - index_x, middle_y - index_y)
                #print(distance)
            threshold=35
            current_time = time.time()
            cooldown=0.4
            
            if distance_index_thumb<threshold:
               if current_time - last_time > cooldown:
                 pyautogui.click(button='left')
                 last_time = current_time
               else:
                   #print("pinch not ready")
                   pass
            if distance_middle_thumb < threshold :
                if current_time - last_time > cooldown:
                 pyautogui.click(button='right')
                 last_time = current_time
                    
            else:
                #print("nothing")
                pass
            

        cv2.imshow("Webcam Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


            