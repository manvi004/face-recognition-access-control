# System Architecture

The Face Recognition Automation System follows a distributed hardware–software architecture to address the computational
limitations of embedded devices.

## Overview
The ESP32-CAM is responsible for image capture and hardware interfacing.
Facial recognition is performed using OpenCV on an external processing unit, while MySQL provides persistent storage for user data and access logs.

## Data Flow
1. ESP32-CAM captures an image when an access request is initiated.
2. The image is transmitted over Wi-Fi to the processing unit.
3. OpenCV performs face detection and recognition.
4. Authentication results are validated against stored user records.
5. The result is returned to the ESP32 for access control action.
6. All access attempts are logged in the database.

## Design Rationale
1. ESP32-CAM is optimized for low-power image capture and GPIO control.
2. OpenCV provides better recognition accuracy and flexibility.
3. MySQL ensures data persistence and scalability.
