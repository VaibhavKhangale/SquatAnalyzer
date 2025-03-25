from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
import cv2
import time
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Global Variables
angle=0
squat_count = 0
squat_down = False
camera_active = False

def calculate_angle(a, b, c):
    """Calculate the knee angle using vector math."""
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.degrees(np.arccos(cosine_angle))

def generate_frames():
    """OpenCV video stream with squat detection logic."""
    global squat_count, squat_down, camera_active,angle
    cap = cv2.VideoCapture(0)
    camera_active = True

    while camera_active:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb_frame)

        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark

            def get_landmark(landmark):
                return int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])

            foot = get_landmark(landmarks[mp_pose.PoseLandmark.LEFT_ANKLE])
            knee = get_landmark(landmarks[mp_pose.PoseLandmark.LEFT_KNEE])
            waist = get_landmark(landmarks[mp_pose.PoseLandmark.LEFT_HIP])

            cv2.circle(frame, foot, 8, (255, 0, 0), -1)
            cv2.circle(frame, knee, 8, (0, 255, 0), -1)
            cv2.circle(frame, waist, 8, (0, 0, 255), -1)

            angle = calculate_angle(foot, knee, waist)

            cv2.putText(frame, f"{int(angle)}°", (knee[0] - 30, knee[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

            # ✅ Squat detection logic
            if angle > 120 and not squat_down:
                squat_down = True  # Squat Started (Going Down)

            elif angle <= 90 and squat_down:
                squat_count += 1
                squat_down = False  # Squat Completed (Standing Up)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

def video_feed(request):
    """Django view to stream video frames."""
    global camera_active
    camera_active = True
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def stop_feed(request):
    """Stop the camera and reset squat count."""
    global camera_active, squat_count, squat_down
    camera_active = False
    squat_count = 0
    squat_down = False
    return JsonResponse({"message": "Camera stopped and squat count reset"})

def squat_count_feed(request):
    """Streaming squat count updates separately from the video feed."""
    def event_stream():
        global squat_count, angle
        previous_count = 0  # Track squat count changes
        previous_message = ""  # Track last message

        while camera_active:
            message = ""  # Default empty message

            # ✅ Send "Get Ready" when a squat attempt starts (angle > 120°)
            if angle > 120 and previous_message != "Get Ready":
                message = "Get Ready"

            # ✅ Send "Go Deeper" when the user is squatting but hasn't completed it yet
            elif angle <= 120 and angle > 90 and previous_message != "Go Deeper":
                message = "Go Deeper"

            # ✅ Send "Nice" when the squat is within the correct range (<= 90°)
            elif angle <= 90 and angle > 60 and previous_message != "Nice":
                message = "Nice"

            # ✅ Send "Perfect" when the squat is very deep (<= 60°)
            elif angle <= 60 and previous_message != "Perfect":
                message = "Perfect"

            # ✅ Send message only if it has changed
            if message and message != previous_message:
                previous_message = message
                yield f"event: squat_message\ndata: {message}\n\n".encode()

            # ✅ Send squat count only when it changes
            if squat_count != previous_count:
                previous_count = squat_count
                yield f"event: squat_count\ndata: {squat_count}\n\n".encode()

            time.sleep(0.5)  # Prevent excessive updates

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")

def home(request):
    """Render the main webpage."""
    return render(request, 'squats/home.html')

