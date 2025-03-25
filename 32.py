import cv2
import numpy as np

img1 = np.zeros((200,320,3), np.uint8)
cv2.line(img1, (0,0), (320,200), (255,0,0),5)
cv2.line(img1, (320,0), (0,200), (0,255,0),5)
cv2.imshow('img',img1)
cv2.waitKey(0)

img2 = np.zeros((200,320,3), np.uint8)
cv2.rectangle(img2, (20,20), (300,180), (255,0,0),5)
cv2.rectangle(img2, (70,70), (250,130), (0,255,0),-1)
cv2.imshow('img2',img2)
cv2.waitKey(0)

img3 = np.zeros((200,320,3), np.uint8)
cv2.circle(img3,(160,100), 80, (0,255,0),5)
cv2.circle(img3,(160,100), 40, (255,0,0),-1)
cv2.imshow('img3',img3)
cv2.waitKey(0)

img4 = np.zeros((200,320,3), np.uint8)+255
cv2.ellipse(img4,(160,100),(120,50),0,0,360,(255,0,0),5)
cv2.ellipse(img4,(160,100),(60,15),0,0,360,(0,255,0),51)
cv2.imshow('img4',img4)
cv2.waitKey(0)

img5 = np.zeros((200,320,3), np.uint8)+255
pts = np.array([[160,20],[20.100],[160,180],[300,100]],np.int32)
cv2.polylines(img5,[pts],True,(255,0,0),5)
pts = np.array([[160,60],[60.100],[160,140],[260,100]],np.int32)
cv2.polylines(img5,[pts],False,(0,255,0),5)
cv2.imshow('img5',img5)
cv2.waitKey(0)

