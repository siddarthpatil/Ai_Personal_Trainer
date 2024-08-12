import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe drawing utilities
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def draw_landmarks(frame, results):
    """
    Draw pose landmarks on the frame.
    """
    mp_drawing.draw_landmarks(
        frame,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
        connection_drawing_spec=mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
    )
    return frame

def draw_angle(frame, angle, position):
    """
    Draw the calculated angle on the frame.
    """
    cv2.putText(frame, str(int(angle)),
                tuple(np.multiply(position, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return frame

def draw_feedback(frame, feedback):
    """
    Overlay feedback text on the frame.
    """
    cv2.putText(frame, feedback, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return frame
