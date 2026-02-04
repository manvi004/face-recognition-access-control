-- Database schema for Face Recognition Automation System

CREATE DATABASE face_recognition_system;
USE face_recognition_system;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE access_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    access_status VARCHAR(20),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
