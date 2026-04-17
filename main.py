import cv2
import os

# Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load known faces
known_faces = []  # list of grayscale images
person_name = "Aqib"
path = f"known_faces/{person_name}"

for img_name in os.listdir(path):
    img_path = os.path.join(path, img_name)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    known_faces.append(img)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 5)

    for (x, y, w, h) in faces:
        face_img = gray_frame[y:y+h, x:x+w]
        name = "Unknown"

        # Compare with known faces
        for img in known_faces:
            resized_face = cv2.resize(face_img, (img.shape[1], img.shape[0]))
            diff = cv2.absdiff(resized_face, img)

            if diff.mean() < 50:  # simple threshold
                name = person_name
                break

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()