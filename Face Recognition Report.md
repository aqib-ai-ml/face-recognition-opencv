{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica-Bold;\f1\fswiss\fcharset0 Helvetica;\f2\fswiss\fcharset0 ArialMT;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0\c84706;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa320\qc\partightenfactor0

\f0\b\fs64 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Face Recognition System (OpenCV)
\f1\b0 \AppleTypeServices \'a0
\f2\fs24 \cb1 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\b\fs42\fsmilli21333 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 Overview
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 
\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 This project is a basic face recognition system built using Python and OpenCV. It detects faces in real-time using a webcam and compares them with stored images to identify whether the detected face matches a known person. Earlier I had wanted to use a Raspberry Pi 5 but it required a monitor and keyboard and mouse, which at the time I did not possess. So I had to make use of my own computer\'92s cpu and made it run the open-cv code. It required a lot of time for me to understand, but at the end I felt that it was worth it.\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f0\b\fs42\fsmilli21333 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Features
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 
\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Real-time face detection using webcam\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Face recognition using pixel-based similarity\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Support for multiple known images\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Displays detected face with label (known/unknown)\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f0\b\fs42\fsmilli21333 \AppleTypeServices\AppleTypeServicesF65539 \cb3 How It Works
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 
\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 The program uses Haar Cascade to detect faces in a video stream.\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Detected faces are converted to grayscale.\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 The detected face is resized and compared with stored images.\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 A similarity check is performed using pixel differences.\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 If the difference is below a threshold, the face is recognized.\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f0\b\fs42\fsmilli21333 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Technologies Used
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 
\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Python\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 OpenCV\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 NumPy\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 OS module\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f0\b\fs42\fsmilli21333 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Project Structure
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 
\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 face-recognition-opencv/\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \uc0\u9474 \u9472 \u9472  known_faces/\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \uc0\u9474  \u9492 \u9472 \u9472  Aqib/\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \uc0\u9474  \u9500 \u9472 \u9472  img1.jpg\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \uc0\u9474  \u9500 \u9472 \u9472  img2.jpg\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \uc0\u9474 \u9472 \u9472  main.py\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \uc0\u9474 \u9472 \u9472  README.md\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f0\b\fs42\fsmilli21333 \AppleTypeServices\AppleTypeServicesF65539 \cb3 How to Run
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 
\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Install dependencies:\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 pip install opencv-python numpy\AppleTypeServices \'a0
\f2\fs24 \cb1 \
\pard\pardeftab720\sa320\partightenfactor0

\f1\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 Add images of the person inside the known_faces/<name> folder.\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f1\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Run the program:\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 python main.py\AppleTypeServices \'a0
\f2\fs24 \cb1 \

\f1\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Press Q to exit the webcam.\AppleTypeServices \'a0
\f2\fs24 \cb1 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\b\fs32 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 Author
\f1\b0 \AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Aqib\AppleTypeServices \'a0\cb1 \uc0\u8232 \AppleTypeServices\AppleTypeServicesF65539 \cb3 Aspiring AI/ML Engineer\AppleTypeServices \'a0
\f2\fs24 \cb1 \
\pard\pardeftab720\sa213\partightenfactor0

\f1\fs32 \cf2 \cb3 \'a0
\f2\fs24 \cb1 \
}
