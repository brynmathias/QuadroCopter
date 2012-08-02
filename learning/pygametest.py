#!/usr/bin/env python
import cv
from PIL import Image,ImageChops
import PIL
import pygame
import pygame.locals as pglocals
import sys
import Utils.ImgUtils as utils
# print help(pygame.locals)
N_FRAMES = 500


def main():
  """example program to capture images from the screen and show them in a pygame window."""
  camera = cv.CreateCameraCapture(0);
  images = []
  fps = 300.0
  window,screen = utils.setUpPyGameWindow()
  run = True
  i = 0
  while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pglocals.QUIT or event.type == pglocals.KEYDOWN:
            print event.type
            break
    im = utils.getImage(captureDevice = camera,Debug = False)    
    images.append(im)
    utils.drawInWindow(im,screen,window)
    i+=1
    if i > N_FRAMES: run = False
  pass
  
  
if __name__ == "__main__":
  main()