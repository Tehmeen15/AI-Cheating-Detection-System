import cv2
import numpy as np
import dlib
import math

# Load face detector and landmark predictor
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Dictionary to store student statuses
student_status = {}

def calculate_eye_aspect_ratio(eye_points):
    # Calculate the vertical distances
    v1 = np.linalg.norm(eye_points[1] - eye_points[5])
    v2 = np.linalg.norm(eye_points[2] - eye_points[4])
    # Calculate the horizontal distance
    h = np.linalg.norm(eye_points[0] - eye_points[3])
    # Calculate the eye aspect ratio
    ear = (v1 + v2) / (2.0 * h)
    return ear

def get_eye_points(landmarks, eye_indices):
    points = []
    for idx in eye_indices:
        points.append(np.array([landmarks.part(idx).x, landmarks.part(idx).y]))
    return np.array(points)

def calculate_gaze_direction(eye_points, face_rect):
    # Calculate the center of the eye
    eye_center = np.mean(eye_points, axis=0)
    
    # Calculate the relative position of the eye center to the face
    face_center_x = (face_rect.left() + face_rect.right()) / 2
    face_center_y = (face_rect.top() + face_rect.bottom()) / 2
    
    # Calculate the angle of gaze
    dx = eye_center[0] - face_center_x
    dy = eye_center[1] - face_center_y
    angle = math.degrees(math.atan2(dy, dx))
    
    return angle

def detect_cheating(frame):
    global student_status
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)
    new_status = {}
    
    # Define eye landmark indices
    LEFT_EYE_INDICES = list(range(36, 42))
    RIGHT_EYE_INDICES = list(range(42, 48))
    
    for i, face in enumerate(faces):
        landmarks = landmark_predictor(gray, face)
        
        # Get eye points
        left_eye_points = get_eye_points(landmarks, LEFT_EYE_INDICES)
        right_eye_points = get_eye_points(landmarks, RIGHT_EYE_INDICES)
        
        # Calculate eye aspect ratios
        left_ear = calculate_eye_aspect_ratio(left_eye_points)
        right_ear = calculate_eye_aspect_ratio(right_eye_points)
        avg_ear = (left_ear + right_ear) / 2.0
        
        # Calculate gaze direction
        left_gaze = calculate_gaze_direction(left_eye_points, face)
        right_gaze = calculate_gaze_direction(right_eye_points, face)
        avg_gaze = (left_gaze + right_gaze) / 2.0
        
        # Draw face and eye markers
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
        
        # Draw eye contours
        cv2.drawContours(frame, [cv2.convexHull(left_eye_points)], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [cv2.convexHull(right_eye_points)], -1, (0, 255, 0), 1)
        
        # Assign unique ID based on face position
        student_id = (face.left(), face.top(), face.right(), face.bottom())
        
        # Determine cheating status based on eye aspect ratio and gaze direction
        is_looking_away = False
        
        # Check if eyes are open (EAR threshold)
        if avg_ear < 0.2:  # Eyes might be closed or partially closed
            status = "Eyes closed"
            color = (0, 0, 255)
        else:
            # Check gaze direction
            if abs(avg_gaze) > 30:  # Looking significantly to the side
                is_looking_away = True
                status = "Looking away"
                color = (0, 0, 255)
            else:
                status = "Focused"
                color = (0, 255, 0)
        
        # Add gaze direction indicator
        gaze_text = f"Gaze: {avg_gaze:.1f}°"
        cv2.putText(frame, gaze_text, (face.left(), face.bottom() + 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        # Add EAR value
        ear_text = f"EAR: {avg_ear:.2f}"
        cv2.putText(frame, ear_text, (face.left(), face.bottom() + 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        new_status[student_id] = (status, color)
        cv2.putText(frame, f"Student {i+1}: {status}", (face.left(), face.top() - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    student_status = new_status
    cv2.putText(frame, "Exam Monitoring: Active", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    return frame

# Start webcam capture
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = detect_cheating(frame)
    cv2.imshow("Cheating Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
