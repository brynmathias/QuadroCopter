#!/usr/bin/env python

import numpy as np
import Utils.ImgUtils as utils
import cv
import pylab

def main():
  """take an image copy it, take the middle slice of one image and scan though the other image until we match.
  Later make in to a function - MatchSlice with slice width that takes any two images. Use for the distance measurement"""
  image = utils.getImage(Debug = True)
  
  image2 = utils.getImage(Debug = True)#cv.CreateImage(cv.GetSize(image),
                     # cv.IPL_DEPTH_8U,3)
  # cv.Copy(image,image2)
  
  size = cv.GetSize(image2)
  split = utils.returnSplitImg(sub_x = int(size[0]/10) , sub_y = size[1], img = image)
  split2 = utils.returnSplitImg(sub_x = int(size[0]/10) , sub_y = size[1], img = image2)
  
  window,screen = utils.setUpPyGameWindow()
  
  testImage = split[int(len(split)/2)]
  cv.SaveImage("testImage.png",testImage)
  
  matched = utils.MatchedImage(testImage,split2)
  print matched.matchedIndex, matched.matchedValue
  for image in matched.compareMats:
    utils.drawInWindow(image,screen,window)
    raw_input()

if __name__=="__main__":
  main()