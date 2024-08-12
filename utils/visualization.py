# utils/visualization.py

import cv2
import numpy as np
import mediapipe as mp

def draw_landmarks(frame, landmarks, pose):
    mp.solutions.drawing_utils.draw_landmarks(
        frame, landmarks, pose.POSE_CONNECTIONS)

def display_feedback(frame, feedback, position=(10, 50), color=(0, 255, 0)):
    cv2.putText(frame, feedback, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
