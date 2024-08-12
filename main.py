import cv2
import mediapipe as mp
from exercises import detect_squat, detect_push_up, detect_bench_press, detect_dips, detect_pull_up, detect_crunches
from utils import draw_landmarks, display_feedback

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize MediaPipe Drawing Utils
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    # Check if pose landmarks are detected
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Detect and provide feedback for different exercises
        feedback_squat, angle_squat = detect_squat(landmarks, mp_pose)
        display_feedback(frame, f'Squat: {feedback_squat} | Angle: {angle_squat}', position=(10, 50))
        
        feedback_push_up, angle_push_up = detect_push_up(landmarks, mp_pose)
        display_feedback(frame, f'Push-Up: {feedback_push_up} | Angle: {angle_push_up}', position=(10, 100))
        
        feedback_bench_press, angle_bench_press = detect_bench_press(landmarks, mp_pose)
        display_feedback(frame, f'Bench Press: {feedback_bench_press} | Angle: {angle_bench_press}', position=(10, 150))
        
        feedback_dips, angle_dips = detect_dips(landmarks, mp_pose)
        display_feedback(frame, f'Dips: {feedback_dips} | Angle: {angle_dips}', position=(10, 200))
        
        feedback_pull_up, angle_pull_up = detect_pull_up(landmarks, mp_pose)
        display_feedback(frame, f'Pull-Up: {feedback_pull_up} | Angle: {angle_pull_up}', position=(10, 250))
        
        feedback_crunches, angle_crunches = detect_crunches(landmarks, mp_pose)
        display_feedback(frame, f'Crunches: {feedback_crunches} | Angle: {angle_crunches}', position=(10, 300))

        # Draw landmarks and connections
        draw_landmarks(frame, results.pose_landmarks, mp_pose)
    
    # Display the resulting frame
    cv2.imshow('Pose Estimation', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and destroy windows
cap.release()
cv2.destroyAllWindows()
