# exercises/squat.py

import numpy as np
from utils.angle_calculation import calculate_angle

def detect_squat(landmarks, pose):
    hip = [landmarks[pose.PoseLandmark.LEFT_HIP.value].x, landmarks[pose.PoseLandmark.LEFT_HIP.value].y]
    knee = [landmarks[pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[pose.PoseLandmark.LEFT_KNEE.value].y]
    ankle = [landmarks[pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[pose.PoseLandmark.LEFT_ANKLE.value].y]
    
    angle = calculate_angle(hip, knee, ankle)
    
    if angle > 160:
        return "Up", angle
    elif angle < 90:
        return "Down", angle
    else:
        return "Intermediate", angle
