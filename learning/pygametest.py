#!/usr/bin/env python
import cv
from PIL import Image,ImageChops
import PIL
import pygame
import pygame.locals as pglocals
import sys
# print help(pygame.locals)
N_FRAMES = 10

def getImage():
  """Set up the camera and pull an image"""
  cv.NamedWindow("camera raw",0)
  capture = cv.CreateCameraCapture(0)
  img = cv.QueryFrame(capture)
  return img
  

images = []
fps = 300.0
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.set_caption("WebCam Demo")
screen = pygame.display.get_surface()
run = True
i = 0
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pglocals.QUIT or event.type == pglocals.KEYDOWN:
            print event.type
            break
    im = getImage()    
    images.append(im)
    src_rgb = cv.CreateMat(im.height, im.width, cv.CV_8UC3)
    cv.CvtColor(im, src_rgb, cv.CV_BGR2RGB)
    # pg_img = pygame.surfarray.array2d(im)
    pg_img = pygame.image.frombuffer(src_rgb.tostring(), cv.GetSize(src_rgb), "RGB")
    screen.blit(pg_img, (0,0))
    pygame.display.flip()
    pygame.time.delay(int(1000 * 1.0/fps))
    i+=1
    if i > N_FRAMES: run = False
    
print images
# a = 0
# for imga,imgb in zip(images,images[1:]):
#   new_img = ImageChops.subtract(imga, imgb)
#   pg_img = pygame.image.frombuffer(new_img.tostring(), new_img.size, new_img.mode)
#   screen.blit(pg_img, (0,0))
#   pygame.display.flip()
#   pygame.time.delay(0)
#   
#   new_img.save("file_%d.jpeg"%(a),"JPEG")
#   a+=1
  # raw_input()