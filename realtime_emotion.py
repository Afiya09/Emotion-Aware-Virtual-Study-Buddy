#built in python module that helps ypu make ypur script accept command line arduments-meaning you can control how your program runs without editing the code
import argparse
#To calculate FPS so you can see how fast your webcam detection is running
import time
#deque -to store a short history of the last few detected emotions to smmooth the results over time
# Counter - to find the most common emotion from the recent history 
from collections import deque,Counter
#opencv-python library for real-time computer vision tasks
import cv2
#openCV stores every image as a NumPy array
import numpy as np

DEFAULT_ENGINE = "deepface"
#Emoji Map
EMOJI_MAP = {
    "angry": "😠",
    "disgust": "🤢",
    "fear": "😨",
    "happy": "😄",
    "sad": "😢",
    "surprised": "😲",
    "neutral": "😐",
    "calm": "😌",
    "confused": "😕",
    "contempt": "😒"

}

#helpers
#frame-the image or video frame(from your webcam). Its a nmmpy array from cv2.VideoCapture
#text-the string to display
#pos-the position (x,y) where the text should be drawn on the frame
#font_sacle-controls how big the text appears
#thickness-controls how thick the text appears
def draw_label(frame,text,pos=(10,30),font_scale=1.0,thickness=2):
    '''Draw filled rectangle behind text for readibility then put Text.'''
    #the pos variable holds where you want to display the text on the frame
    x,y=pos
    #It is one of openCV's built-in fonts . Used for both cv2.putText and cv2.getTextSize
    font = cv2.FONT_HERSHEY_SIMPLEX
    #draw a background rectangle
    (w,h),_= cv2.getTextSize(text,font,fontScale=font_scale,thickness=thickness)
    #background rectangle-filled black rectangle
    cv2.rectangle(frame,pos,(x-5,y-h-5),(x+w+5,y+5)(0,0,0),cv2.FILLED)
    #this draws the actual text on top of the rectangle
    #cv2.LINE_AA -antialiased line for better quality
    cv2.putText(frame,text,(x,y),font,font_scale,(255,255,255),thickness,cv2.LINE_AA)
