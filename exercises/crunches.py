# exercises/crunches.py

import numpy as np
from utils.angle_calculation import calculate_angle

def detect_crunches(landmarks, pose):
    hip = [landmarks[pose.PoseLandmark.LEFT_HIP.value].x, landmarks[pose.PoseLandmark.LEFT_HIP.value].y]
    shoulder = [landmarks[pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[pose.PoseLandmark.LEFT_ELBOW.value].y]
    
    angle = calculate_angle(hip, shoulder, elbow)
    
    if angle > 160:
        return "Up", angle
    elif angle < 90:
        return "Down", angle
    else:
        return "Intermediate", angle
