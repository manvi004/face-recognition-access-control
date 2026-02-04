"""
Face Recognition Processing Service

This module represents the server-side logic of the
Face Recognition Automation System.

Responsibilities:
- Receive image frames from ESP32-CAM
- Perform face detection and recognition using OpenCV
- Validate recognized users against a MySQL database
- Log all access attempts
"""

import mysql.connector
import cv2   # OpenCV library


# Load face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Load face recognizer (example: LBPH)
recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read("trained_model.yml")  # Loaded during actual deployment


def connect_database():
    """
    Establish connection to the MySQL database.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="face_recognition_system"
    )


def recognize_face(image_frame):
    """
    Perform face detection and recognition on the received image.

    Args:
        image_frame: Image captured by ESP32-CAM

    Returns:
        user_id (int): ID of recognized user
        None: if no valid face match is found
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face_region = gray[y:y+h, x:x+w]

        # Predict user ID using trained recognizer
        user_id, confidence = recognizer.predict(face_region)

        # Lower confidence value indicates better match
        if confidence < 60:
            return user_id

    return None


def is_registered_user(cursor, user_id):
    """
    Check whether the recognized user exists in the database.
    """
    query = "SELECT user_id FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() is not None


def log_access(cursor, user_id, status):
    """
    Log access attempt (GRANTED / DENIED) in the database.
    """
    query = """
        INSERT INTO access_logs (user_id, access_status)
        VALUES (%s, %s)
    """
    cursor.execute(query, (user_id, status))


def process_request(image_frame):
    """
    Main processing workflow:
    1. Receive image from ESP32-CAM
    2. Detect and recognize face using OpenCV
    3. Validate user against database
    4. Log access attempt
    5. Return authentication result
    """
    db = connect_database()
    cursor = db.cursor()

    user_id = recognize_face(image_frame)

    if user_id and is_registered_user(cursor, user_id):
        log_access(cursor, user_id, "GRANTED")
        access_granted = True
    else:
        log_access(cursor, None, "DENIED")
        access_granted = False

    db.commit()
    db.close()

    return access_granted
