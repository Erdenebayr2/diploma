import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def mediapipe_detection(image,model):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    return image, results

def draw_landmarks(image, results):
    if results.face_landmarks:
        mp_drawing.draw_landmarks(image, results.face_landmarks)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS)

def draw_style_landmarks(image, results):
    if results.face_landmarks:
        mp_drawing.draw_landmarks(image, results.face_landmarks,mp_holistic.HAND_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                                mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1))
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2), 
                                  mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2), 
                                  mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))

cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        flip_frame = cv2.flip(frame,1)

        image, results = mediapipe_detection(flip_frame,holistic)

        draw_style_landmarks(image, results)

        cv2.imshow('open cv', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

draw_landmarks(flip_frame,results )
plt.imshow(cv2.cvtColor(flip_frame,cv2.COLOR_BGR2RGB))