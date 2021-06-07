# Rock Paper Scissors 

Rock Paper Scissors is a well known game for two players. For each player, there are three choices- Rock, Paper or Scissors. Rock beats Scissors, Paper beats Rock and Scissors beats Paper. Players choose their moves and if both players make the same move, the game is tied. Else the winner is decided on the above rules.   

This simple game is implemented using computer vision. It works on the fact that for gestures of rock, paper and scissors, 0, 5, 2 fingers (respectively) are raised up.  


HandTrackingModule.py is used to detect hands in the camera frame and fingercounter.py (modified) to count the number of fingers raised up. 

## Changes made in FingerCounter.py:
1. A separate function countFingers() is created for counting the fingers that takes landmarks of hand (provided by HandTrackingModule) as an argument and returns the total number of fingers that are up.
2. A main() function that contains piece of code which gets executed only when fingercounter.py is run and not when any other python file omporting this file is run. 

## Prerequisites to run the program:
Python 2 or 3 along with cv2 and mediapipe must be present in the system.

## Working of RockPaperScissors.py
- Predefined modules - cv2, time, os, random 
- User defineds modules - HandTrackerModule as htm, fingercounter as fc  

1. Webcam window with the name "Rock Paper Scissors" is started and two boxes are drawn - left for user and right for computer.
2. FPS counter is constantly running in the bottom left corner of webcam window.
3. If user brings hand inside left box, handtracking is started.
4. detector object of htm module returns the landmarks of the palm and countFingers function of fc module returns the count of fingers raised and assigned to user.
5. randint function of random module returns a random integer between 0 and 2 (both inclusive) and assigns it to computer.
6. If 1, 3 or 4 fingers are raised by the user, nothing happens.
7. However, if 0, 2 or 5 fingers are raised, the winner (or tie) is decided using win_dict.
8. Image of rock, paper, scissors for computer is shown in the right box.
9. Moves of both the players are shown under the boxes.
10. The result is shown in top portion of the window.
11. Most of the text is centre aligned using alignText function that takes necessary arguments to calculate the position of x-coordinate (from where to start printing).
12. Window can be exited by either stopping the program or pressing 'q' or 'Q' (keyboard interrupt).
