# Limitations and Improvements

## Base Implementation Limitations

1. On-device face recognition on ESP32-CAM showed limited accuracy.
2. Facial data was lost after power cycles due to a lack of persistence; even with a memory slot in the ESP32, it was not scalable.
3. System scalability was restricted to a small number of users.

## Improved Design Considerations

1. Offloading facial recognition to OpenCV improves robustness.
2. Database-backed storage ensures persistent user data and enables the auditing process as well.
3. Separation of capture and processing enhances maintainability.
