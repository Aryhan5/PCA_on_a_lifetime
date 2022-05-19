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

def import_picture(path):
    image = cv2.imread(path)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grey

def extract_from_observation(raw_results):
    cleaned_data = list(map(lambda x : {"ID": x.tag_id, "centroid":x.center}, raw_results))
    df = pd.DataFrame(cleaned_data)
    df.set_index('ID')
    return df

def get_coord_from_picture(path):
    img = import_picture(path)
    det_results = detect(img)
    coord = extract_from_observation(det_results)
    return coord


