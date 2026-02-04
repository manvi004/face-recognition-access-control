This module performs face detection and recognition using OpenCV.
It processes images received from the ESP32-CAM and determines authentication outcomes in real time.
This directory represents the server-side processing layer
of the Face Recognition Automation System.

OpenCV is used for face detection and recognition, while Python
acts as the integration layer between image processing and the
database.

## Responsibilities:
1. Receive images from ESP32-CAM
2. Perform face detection and recognition
3. Validate users against stored records
4. Return authentication results
5. Trigger access logging
