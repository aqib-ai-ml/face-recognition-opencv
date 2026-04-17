Face Recognition System (OpenCV) 

Overview 
This project is a basic face recognition system built using Python and OpenCV. It detects faces in real-time using a webcam and compares them with stored images to identify whether the detected face matches a known person. Earlier I had wanted to use a Raspberry Pi 5 but it required a monitor and keyboard and mouse, which at the time I did not possess. So I had to make use of my own computer’s cpu and made it run the open-cv code. It required a lot of time for me to understand, but at the end I felt that it was worth it. 

Features 
Real-time face detection using webcam 
Face recognition using pixel-based similarity 
Support for multiple known images 
Displays detected face with label (known/unknown) 

How It Works 
The program uses Haar Cascade to detect faces in a video stream. 
Detected faces are converted to grayscale. 
The detected face is resized and compared with stored images. 
A similarity check is performed using pixel differences. 
If the difference is below a threshold, the face is recognized. 

Technologies Used 
Python 
OpenCV 
NumPy 
OS module 

Project Structure 
face-recognition-opencv/ 
│── known_faces/ 
│ └── Aqib/ 
│ ├── img1.jpg 
│ ├── img2.jpg 
│── main.py 
│── README.md 

How to Run 
Install dependencies: 
pip install opencv-python numpy 

Add images of the person inside the known_faces/<name> folder. 

Run the program: 
python main.py 

Press Q to exit the webcam. 

Author 
Aqib 
Aspiring AI/ML Engineer 

 
