# pip install opencv-python
# install this through microsoft visual studio-pip install cmake
# pip install "C:\Users\Syed Usama Kazmi\Desktop\FacialAndSpeechRecognition\dlib-19.19.0-cp38-cp38-win_amd64.whl"
# pip install face-recognition

# dlib file video https://www.youtube.com/watch?v=AUJKdehF2ZA

import cv2
import face_recognition

img = cv2.imread("images/usama.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/kazmi.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)
