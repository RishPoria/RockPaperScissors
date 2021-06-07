import cv2
import time
import os
import random
import HandTrackingModule as htm
import fingercounter as fc


def alignText(text, scale, thickness, xright):
    textsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, scale, thickness)[0]
    textX = (xright - textsize[0]) // 2
    return textX


def main():
    wCam, hCam = 640, 480
    wbox, hbox = 240, 320
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "GameImages"
    myList = os.listdir(folderPath)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)

    pTime = 0
    detector = htm.handDetector(detectionCon=0.75)
    comp_dict = {0:0, 1:2, 2:5}
    win_dict = {0:2, 2:5, 5:0}
    rps = {0:'Rock', 2: 'Scissors', 5: 'Paper'}
    prev_user = None

    while True:
        success, img = cap.read()
        img[80:400, 40:280] = detector.findHands(img[80:400, 40:280])
        cv2.rectangle(img, (40, 80), (280, 400), (0, 0, 0), 2)
        cv2.rectangle(img, (360, 80), (600, 400), (0, 0, 0), 2)
        lmList = detector.findPosition(img[80:400, 40:280], draw=False)
        if len(lmList) != 0:
            user = fc.countFingers(lmList)
            if prev_user == None or prev_user != user:
                prev_user = user
                comp = random.randint(0,2)

            if user in (1, 3, 4):
                pass
            else:
                if user == comp_dict[comp]:
                    # print(f"It's a Tie, both chose {rps[user]}.")
                    text = "IT'S A TIE"

                elif win_dict[user] == comp_dict[comp]:
                    # print(f"You win. {rps[user]} beats {rps[comp_dict[comp]]}.")
                    text = "YOU WIN"
                else:
                    # print(f"Computer wins. {rps[comp_dict[comp]]} beats {rps[user]}.")
                    text = "COMPUTER WINS"


                cv2.putText(img, text, (alignText(text, 4, 6, wCam), 58), cv2.FONT_HERSHEY_PLAIN, 4, (181, 16, 126), 6)

                img_resize = cv2.resize(overlayList[comp], (wbox,hbox))

                img[80: 400, 360:600] = img_resize
                cv2.putText(img, str(rps[user]), (alignText(str(rps[user]), 2, 2, 320), 440), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
                cv2.putText(img, str(rps[comp_dict[comp]]), (320 + alignText(str(rps[comp_dict[comp]]), 2, 2, 320), 440), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (30, 465), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)

        cv2.imshow("Rock Paper Scissors", img)
        if cv2.waitKey(1) & 0xFF in (ord('q'), ord('Q')):
            break


if __name__ == "__main__":
    main()
