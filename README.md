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

1) Import the CV module.

2) Capture the Object. 

3) Read and Display the image.

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
 
 <h3> • Overlay </h3>
Overlay process consists of -

1) Creating a white square box using Numpy
2) Finding the ratio between height and width
3) Resizing the image according to ratio and place it inside the white box
4) Saving images of respected sign

| ![image](https://user-images.githubusercontent.com/111730373/203127300-e1dbb85c-e879-4819-bf64-c9ee798cbec2.png) |  
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  Image resizing                                                  |  

After Resizing everything else is done what’s left is to capture the hand signs and save it.

To capture an image we -

1) First create a folder and store its location in any variable.
  
2) Assign a key to capture image.

3) Use imwrite function to write/store the images along with an image name.

| ![image](https://user-images.githubusercontent.com/111730373/203128179-80858267-0fcd-4a82-b8ed-779b17afeaba.png) |  
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  Writing/ Storing images                                         |


<h3> • Data Collection </h3>

Now the code for data collection is complete , now we capture 100-300 images of each sign in different ways and store it .
Go to the Teachable Machine site upload all your images and create a data model to compare and test images.
The model obtained is of Keras type.


| ![image](https://user-images.githubusercontent.com/111730373/203128427-63327e3a-605c-43ae-bf40-7ff63678088c.png) | 
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  Training Model                                                  |


<h3> • Testing Code </h3>
( To create the testing code copy the data collection code except the image saving part )

1) Install the tensorflow package.

2) Import Classifier from cvzone.

3) Make your data model act as classifier.

4) Make Prediction by comparing the image with model images the one with most match is displayed.

| ![image](https://user-images.githubusercontent.com/111730373/203129615-f54e4ca6-a3aa-4f40-a1be-57b15c8209a5.png) |   
| :--------------------------------------------------------------------------------------------------------------: |
|                                              Importing Classifier                                                |

| ![image](https://user-images.githubusercontent.com/111730373/203130006-3be5e045-b606-4243-bc7e-7dc8f1a1ea61.png) |   
| :--------------------------------------------------------------------------------------------------------------: |
|                                              Predcition of the sign                                              |



<h3> • Results </h3>

| ![image](https://user-images.githubusercontent.com/111730373/203130577-7caa7c9c-1fcc-4efd-8d62-4c847c28fd3e.png) |   
| :--------------------------------------------------------------------------------------------------------------: |
|                                                  A                                                               |


## :rocket: Resources:

- [Keras Module](https://keras.io/)
- [TensorFlow install](https://www.tensorflow.org/install)
- [Teaching Machine Tool](https://teachablemachine.withgoogle.com/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [American Sign Language](https://en.wikipedia.org/wiki/American_Sign_Language)
- [Icons/Emojis](https://emojipedia.org/)
















 





