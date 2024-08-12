from flask import Flask, render_template, request, Response
import cv2
import numpy as np
import mediapipe as mp
from exercises.squat import detect_squat
from exercises.push_up import detect_push_up
from exercises.bench_press import detect_bench_press
from exercises.dips import detect_dips
from exercises.pull_up import detect_pull_up
from exercises.crunches import detect_crunches
from utils.angle_calculation import calculate_angle
from utils.visualization import draw_landmarks, draw_feedback, draw_angle

app = Flask(__name__)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def detect_exercise(frame, exercise):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        feedback, angle = None, None

        if exercise == 'squat':
            feedback, angle = detect_squat(landmarks, mp_pose)
        elif exercise == 'pushup':
            feedback, angle = detect_push_up(landmarks, mp_pose)
        elif exercise == 'benchpress':
            feedback, angle = detect_bench_press(landmarks, mp_pose)
        elif exercise == 'dips':
            feedback, angle = detect_dips(landmarks, mp_pose)
        elif exercise == 'pullup':
            feedback, angle = detect_pull_up(landmarks, mp_pose)
        elif exercise == 'crunches':
            feedback, angle = detect_crunches(landmarks, mp_pose)

        return feedback, angle, results

    return None, None, None

def generate_frames(exercise):
    cap = cv2.VideoCapture(0)
    
    while True:
        success, frame = cap.read()
        if not success:
            break

        feedback, angle, results = detect_exercise(frame, exercise)
        frame = draw_landmarks(frame, results)
        if angle:
            # Specify the position where you want to display the angle
            position = [0.5, 0.5]  # Example position (relative coordinates)
            frame = draw_angle(frame, angle, position)
        frame = draw_feedback(frame, feedback)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    exercise = request.args.get('exercise', 'squat')  # Default to 'squat'
    return Response(generate_frames(exercise),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
