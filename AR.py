'''
Reconaissance d'apriltag, identification, mise à l'échelle spatiale
'''

import sys
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pupil_apriltags import Detector

from pathlib import Path
import sys

import moms_apriltag as apt

def generate(rng, scale=7): #Scale up 7x for an aprox 1.5cm tag
    tags = apt.generate("tag36h11", range(1, rng+1)) #range below 587 
    for tag in tags:
        img = 255*tag.array
        
        width = int(img.shape[1] * scale)
        height = int(img.shape[0] * scale)
        dim = (width, height)

        scaled = cv2.resize(img, dim, fx=0, fy=0, interpolation = cv2.INTER_NEAREST)
        name = "tags/"+str(tag.id).zfill(3)+".png"
        cv2.imwrite(name, scaled)

def detect(picture):
    apt_detector = Detector(families='tag36h11')
    tags = apt_detector.detect(picture)
    return tags


def identify():
    print()

def scale(map1, map2):
    print()

img = cv2.imread('../stockapril.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tags = detect(gray)
print(tags)