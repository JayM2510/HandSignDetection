<h1 align="center">Hand Sign Detection System
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) 
</h1>

## 💡Overview:
In this sign language recognition project, we create a   sign detector, which detects alphabets that can very easily be extended to cover a vast multitude of other signs and hand gestures including numbers.

We have developed this project using OpenCV and Keras modules of python.

`Hand Sign Detection` 

Hand detection is a crucial pre-processing procedure for many human hand related computer vision tasks, such as hand pose estimation, hand gesture recognition, human activity analysis, and so on.
Hand Gesture recognition technology  would allow for the operations of complex machines using only series of a finger and hand movements, eliminating the need of physical contact between operator and machine.

`American Sign Language`

It is a complete, natural language that has the same linguistic properties as spoken languages, with grammar that differs from English. ASL is expressed by movements of the hands and face.

## 🧰Prerequisites:

`Python` : Python is a high-level, general-purpose programming language.

`PyCharm` : JetBrains PyCharm is a Python IDE.

`Numpy` : NumPy is a library for the Python programming language.

`CV2(Open CV)` : OpenCV is a library of programming functions mainly aimed at real-time computer vision.

`Keras` : Keras is the high-level API of TensorFlow.

`Tensorflow` : TensorFlow is a free and open-source software library for machine learning and artificial intelligence

## 🖊️Working :

<h3> • Starting the Webcam </h3>

Import the CV module.

Capture the Object. 

Read and Display the image.

| ![image](https://user-images.githubusercontent.com/111730373/203122330-ea1eb928-02eb-4514-a986-518518b6b6d4.png) | 
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  Code For webcam                                                 |              

<h3> • Displaying Hand </h3>

To detect a hand in the image we import HandDetector from cvzone and fix the number of hands as One.
In it we also get the skeleton (joins and dots) which helps in recognition.

| ![image](https://user-images.githubusercontent.com/111730373/203122640-f0628451-a41b-4655-b815-773eff784f70.png) | 
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  Displaying Hand Code                                            |   

<h3> • Cropping Hand Image </h3>
 In order to crop hand from the image we have to :
 
1) Store the square image.

2) Get the width and height of the bounded box (bbox).

3) Create another image with the height and width of bounded box.

4) If there is no hand present the cropped image collapses.

| ![image](https://user-images.githubusercontent.com/111730373/203125839-9a91d264-be33-44fc-9d9d-81b196a01f68.png) |  
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  Cropped Hnad Image                                              |  
 














 





