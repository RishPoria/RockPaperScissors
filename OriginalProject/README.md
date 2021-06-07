The original project was developed by the owner of the Youtube channel [Murtaza's Workshop - Robotics and AI](http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI)  
He has made two Python files that help:
1. Detecting the hand using computer vision.
2. Counting the number of fingers that are up at that particular time. 


### Hand Tracking Module
This python file is used for hand tracking in real time.

### Finger Counter 
This python file is used to count the number of fingers that are up.

## Frameworks used:
#### 1. [Mediapipe](https://google.github.io/mediapipe/solutions/hands.html) 

Mediapipe was developed by Google and it has various models which help us to solve very fundamental AI problems.  Few on them are:
- Face Detection
- Facial Landmarks
- Hand Tracking 
- Object Detection

The Hand Tracking model uses two modules at the backend:
1. Palm Detection - Takes a complete image and returns a [cropped image](https://github.com/RishPoria/RockPaperScissors/blob/main/OriginalProject/CroppedImage.jpg) which contains the palm.
2. Hand Landmark - Takes the cropped image and returns [21 landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png) 


#### 2. [OpenCV](https://opencv.org/)

OpenCV is open source and is free for commercial use. It is a cross-platform library includes computer vision algorithms including:
- Image Processing
- Video Analysis
- Camera Calibration and 3D Reconstruction
- Object Detection
  
  
 

## Source code: 
- [CVZONE](https://www.computervision.zone/)
- [Hand Tracking Module](https://github.com/RishPoria/RockPaperScissors/blob/main/OriginalProject/HandTrackingModule.py)
- [Finger Counter](https://github.com/RishPoria/RockPaperScissors/blob/main/OriginalProject/FingerCounter.py)
