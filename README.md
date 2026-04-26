# Face Recognition System (OpenCV)

##  Overview
This project is an early computer vision face recognition prototype using OpenCV. It detects faces in real-time using a webcam and compares them with stored images to identify whether the detected face matches a known person.

Earlier, I planned to use a Raspberry Pi 5. However, it required a monitor, keyboard, and mouse, which I did not have at the time. So I used my personal computer instead to run the OpenCV-based implementation.

It took time to understand and build, but the final result made the effort worthwhile.

---

## Features
- Real-time face detection using webcam  
- Face recognition using pixel-based similarity  
- Support for multiple known images  
- Displays detected face with label (Known / Unknown)  

---

## How It Works
- Uses Haar Cascade to detect faces in video stream  
- Converts detected faces to grayscale  
- Resizes the face for comparison  
- Compares with stored images using pixel difference  
- If difference is below threshold, face is recognized  

---

## Technologies Used
- Python  
- OpenCV  
- NumPy  
- OS module  

Aqib 
