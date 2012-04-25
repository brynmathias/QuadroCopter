#!/usr/bin/env python
import cv

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
subSize = 32
i = 0

for y in range(cv.GetSize(img)[1]/subSize):
  for x in range(cv.GetSize(img)[0]/subSize):
    a = cv.GetSubRect(gray, (x*subSize, y*subSize, subSize,subSize)) 
    cv.SaveImage("sub%i.png"%i,a)
    cv.SetZero(a)
    cv.SaveImage("bar%i.png"%i, gray)    
    i+=1