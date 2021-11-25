#!/usr/bin/env python
# coding: utf-8

# In[25]:


import cv2
import mediapipe as mp
import time
import smtplib
from email.mime.text import MIMEText

def mailer():
    body = "Your House is in dangeour"
    msg = MIMEText(body)
    msg['From'] = "puspendu.kvy@gmail.com"
    msg['To'] = "arabinda281265@gmail.com"
    msg['Subject'] = "Hello"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("puspendu.kvy@gmail.com","Arabinda@19651")
    server.send_message(msg)
    print("Mail sent")
    server.quit()
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            if id==15 and lm.visibility>0.09 and lm.x>0.6 and lm.x<1 and lm.y>0.6 and lm.y<0.9:
                print(lm.x,lm.y)
                mailer()
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




