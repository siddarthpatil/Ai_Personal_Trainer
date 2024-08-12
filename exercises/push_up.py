# exercises/push_up.py

import numpy as np
from utils.angle_calculation import calculate_angle

def detect_push_up(landmarks, pose):
    shoulder = [landmarks[pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[pose.PoseLandmark.LEFT_WRIST.value].y]
    
    angle = calculate_angle(shoulder, elbow, wrist)
    
    if angle > 160:
        return "Up", angle
    elif angle < 90:
        return "Down", angle
    else:
        return "Intermediate", angle
