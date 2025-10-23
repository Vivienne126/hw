import cv2
import mediapipe as mp
import time
import numpy as np

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.7 , min_tracking_confidence=0.7)
mp_draw=mp.solutions.draw_utils

#Filter
filters=[None , "grayscale" , "sepia" , "negative" , "blur"]
current_filter=0

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Could not access the web cam")
    exit()

last_action_time=0
rebounce_time=1

#Fuction to appy filter

def apply_filter(frame, ftype):
    #Apply the specified filter to the frame
    if ftype == 'GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif ftype == 'SEPIA':
        sepia_filter = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        return np.clip(cv2.transform(frame, sepia_filter), 0, 255).astype(np.uint8)
    elif ftype == 'NEGATIVE':
        return cv2.bitwise_not(frame)
    elif ftype == 'BLUR':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame

while True:
    success,ing=cap.read()
    if not success:
        print("Failed to read image from webcam")
        break
    ing=cv2.flip(ing,1)
    ing_rgb=cv2.cvtColor(ing , cv2.COLOR_BGR2RGB)
    results=hands.process(ing_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(ing,hand_landmarks , mp_hands.HAND_LANDMARKS)
            thumb_tip=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            Index_tip=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            Middle_tip=hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            Ring_tip=hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            Pinky_tip=hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_FINGER_TIP]

            #Frame Dimensions
            frame_height , frame_width , _=ing.shape
            