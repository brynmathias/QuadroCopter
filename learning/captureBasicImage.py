#!/usr/bin/env python
import cv2
import numpy
import scipy



def main():
  # """docstring for main"""
  camera = cv2.VideoCapture()
  camera.open(0)
  retval, image = camera.retrieve()
  camera.release()
  # print image
  # for thing in image:
    # print thing
  print image.size
  # print help(image)
  cv2.imwrite("test.png", image)


if __name__ == "__main__":
  main()