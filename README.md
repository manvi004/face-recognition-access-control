# Face Recognition Automation System

# Overview
A face recognition–based automation system designed for secure access control.
This system integrates an ESP32-CAM for image capture and hardware control,
OpenCV for real-time recognition, and MySQL for persistent storage of user data and access logs.

# System Architecture
ESP32-CAM → OpenCV (Python) → MySQL

# Key Components
1. ESP32-CAM: It captures facial images, handles Wi-Fi communication, and interfaces with external control hardware through GPIO.
2. OpenCV (Python): It performs face detection and recognition to authenticate users.
3. MySQL Database: It stores registered user information and logs all access attempts.
4. Control Interface: A relay-based output mechanism used to trigger access actions upon successful authentication.

# Working Flow
1. The ESP32-CAM captures an image when access request is initiated.
2. The image is transmitted over Wi-Fi to an OpenCV-based processing unit.
3. OpenCV performs face detection and recognition in real time.
4. Authentication results are validated using stored records in the MySQL database.
5. Based on authentication outcome, ESP32 triggers an extrernal control signal.
6. All access attempts are logged in database for monitoring and review.

# Observed Limitations of the Base Implementation
1. The base implementation with ESP32 CAM module and relay module has limited face recognition accuracy.
2. There was loss of enrolled face data after power cycles due to lack of persistent storage.
3. There was restricted scalability for multiple users.

# Upgraded Design Approach
1. Facial Recognition was offloaded to OpenCV to improve accuracy and reliability.
2. Database introduced to ensure data persistence.
3. This enabled support for multiple users and access logging.

# Tech Stack
1. ESP32-CAM
2. OpenCV (Python)
3. MySQL

# Note
The base system was initially implemented during undergraduate studies.
This repository documents an upgraded and recreated design focused on system architecture and hardware–software integration.

