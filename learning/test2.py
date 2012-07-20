#!/usr/bin/env python
import cv


from Utils.ImgUtils import returnSplitImg
cv.NamedWindow("camera raw",0)
capture = cv.CreateCameraCapture(0)
img = cv.QueryFrame(capture)
cv.ShowImage("camera raw",img)
cv.SaveImage("foo.png", img)
gray = cv.CreateImage(cv.GetSize(img),
                      cv.IPL_DEPTH_8U,1)


edges = cv.CreateImage(cv.GetSize(img),
                      cv.IPL_DEPTH_8U,1)


cv.CvtColor(img,gray,cv.CV_RGB2GRAY)
cv.SaveImage("bar.png", gray)
cv.Canny(gray,edges,0,100,3)
cv.SaveImage("foobar.png",edges)
print cv.GetSize(img)
x_y = cv.GetSize(img)
subSize = 32
i = 0




someList = returnSplitImg(sub_x = 32, sub_y = 480, img = gray)
for i,a in enumerate(someList): cv.SaveImage("loopTest%i.png"%i,a)

centerImg = someList[int(len(someList)/2)]
cv.SaveImage("CenterImage.png",centerImg)
# for a in cv.cv2array(centerImg): print a
