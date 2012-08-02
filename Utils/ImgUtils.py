#!/usr/bin/env python
import cv
import pygame
import time
import numpy as np
import operator
def returnSplitImg(sub_x = None, sub_y = None, img = None):
  """Split an image up in to N sub pictures of x = sub_x and y = sub_y"""
  imgSize = cv.GetSize(img)
  if sub_x is None: sub_x = imgSize[0]
  if sub_y is None: sub_y = imgSize[1]
  out = []
  for x in range(imgSize[0]/sub_x):
    for y in range(imgSize[1]/sub_y):
      subImg = cv.GetSubRect(img,(sub_x*x,sub_y*y,sub_x,sub_y))
      out.append(subImg)
  return out
  
  
  
def getImage(captureDevice= None,Debug = False):
  """Set up the camera and pull an image"""
  image = cv.QueryFrame(captureDevice)
  image2 = cv.CreateImage(cv.GetSize(image),
                      cv.IPL_DEPTH_8U,3)
  cv.Copy(image,image2)
  if Debug:
    cv.SaveImage("imageAt_%s.png"%time.strftime("%a_%d_%b_%Y_%H:%M:%S"),image2)
  
  return image2



def canny(img = None):
  """take an image and run the canny filter on it"""
  edges = cv.CreateImage(cv.GetSize(img),
                        cv.IPL_DEPTH_8U,1)
  
  cv.Canny(gray,edges,0,100,3)
  return edges


def grayScale(img = None):
  """take an image and convert it to gray scale"""
  gray = cv.CreateImage(cv.GetSize(img),
                        cv.IPL_DEPTH_8U,1)
  cv.CvtColor(img,gray,cv.CV_RGB2GRAY)
  return gray


def setUpPyGameWindow():
  pygame.init()
  window = pygame.display.set_mode((640,480))
  pygame.display.set_caption("windowName")
  screen = pygame.display.get_surface()
  return window,screen
  
def drawInWindow(img = None,screen = None, window = None):
  toDisplay = cv.CreateMat(img.height, img.width, cv.CV_8UC3)
  cv.CvtColor(img, toDisplay, cv.CV_BGR2RGB)
  pg_img = pygame.image.frombuffer(toDisplay.tostring(), cv.GetSize(toDisplay), "RGB")
  screen.blit(pg_img, (0,0))
  pygame.display.flip()
  pygame.time.delay(int(1000 * 1.0/30.))


class MatchedImage(object):
  """docstring for MatchedImage"""
  def __init__(self, target = None, test = None ):
    self.target = target
    self.test = test
    self.matched = None
    self.matchedIndex = None
    self.matchedValue = None
    self.targetMat = cv.GetMat(self.target)
    self.compareMats = []
    self.dets = []

    self.Match()
    self.subedImage = self.compareMats[self.matchedIndex]    
    
  def Match(self):
    """docstring for fname"""
    # First check that the test images are a list
    assert isinstance(self.test,list), "Must have a list of images to compare against"
    for test_i in self.test:
      assert cv.GetSize(self.target) == cv.GetSize(test_i), "images must be the same size!!"
      test_mat = cv.GetMat(test_i)
      compareMat = cv.CreateImage(cv.GetSize(self.target),
                        cv.IPL_DEPTH_8U,3)
      
      cv.AbsDiff(self.targetMat,test_mat,compareMat)
      #Above gets us the abs diff. Now we loop though the numpy representation of this difference.
      # Find the minimum value and call this the match
      sumOfDets = 0
      self.compareMats.append(compareMat)
      for a in np.asarray(cv.GetMat(compareMat)):
        for b in a:
          for c in b: sumOfDets += c
      self.dets.append(sumOfDets)
    self.matchedIndex, self.matchedValue = min(enumerate(self.dets), key=operator.itemgetter(1))
    self.matched = self.test[self.matchedIndex]
      
  pass
