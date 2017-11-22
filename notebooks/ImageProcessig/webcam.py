# Python | 開啟 webcam 電腦鏡頭 – Hello,I AM A PROGRAMMER 
# https://studentcodebank.wordpress.com/2015/08/25/python-%E9%96%8B%E5%95%9F-webcam-%E9%9B%BB%E8%85%A6%E9%8F%A1%E9%A0%AD/

# Reading and Writing Images and Video — OpenCV 2.4.13.4 documentation 
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-release

#import from lib
import cv2

# local modules
#from video import create_capture

if __name__ == '__main__':
   cam = cv2.VideoCapture(0)  #開啟webcam
   while True:
       ret, img = cam.read()
       cv2.imshow('facedetect', img) #開啟一個叫做facedetect的視窗，內容為img
       if 0xFF & cv2.waitKey(5) == 27:
         break
cv2.destroyAllWindows() #關閉所有視窗(好習慣)
cam.release() #關閉 webcam

