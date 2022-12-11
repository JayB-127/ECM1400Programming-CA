# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy as np
from matplotlib import pyplot as mat_plot
from matplotlib import cm


def find_red_pixels(*args,**kwargs):
    # TODO: documentation

    filename = args[0]
    upperThresh = kwargs["upper_threshold"]
    lowerThresh = kwargs["lower_threshold"]

    rgb_img = mat_plot.imread(filename) #per row, per column, rgba values
    rgb_img *= 255 #scale rgb values

    height = len(rgb_img) #rows
    width = len(rgb_img[0]) #columns
    #2d numpy array size of map img
    binaryImg = np.zeros([height, width], dtype = int)

    rowCount = 0
    for i in rgb_img: #for each row
        pixelCount = 0
        for j in i: #for each pixel in row
            if j[0] > upperThresh and j[1] < lowerThresh and j[2] < lowerThresh:
                #set pixel in binary img to white
                binaryImg[rowCount][pixelCount] = 1
            else:
                #set pixel in binary img to black
                binaryImg[rowCount][pixelCount] = 0
            pixelCount += 1
        rowCount += 1

    mat_plot.imsave("data/map-red-pixels.jpg", binaryImg, cmap = cm.gray)
    print("[Found all red pixels and saved binary image to data folder]")

    return binaryImg


def find_cyan_pixels(*args,**kwargs):
    # TODO: documentation

    filename = args[0]
    upperThresh = kwargs["upper_threshold"]
    lowerThresh = kwargs["lower_threshold"]

    rgb_img = mat_plot.imread(filename) #per row, per column, rgba values
    rgb_img *= 255 #scale rgb values

    height = len(rgb_img) #rows
    width = len(rgb_img[0]) #columns
    #2d numpy array size of map img
    binaryImg = np.zeros([height, width], dtype = int)

    rowCount = 0
    for i in rgb_img: #for each row
        pixelCount = 0
        for j in i: #for each pixel in row
            if j[0] < lowerThresh and j[1] > upperThresh and j[2] > upperThresh:
                #set pixel in binary img to white
                binaryImg[rowCount][pixelCount] = 1
            else:
                #set pixel in binary img to black
                binaryImg[rowCount][pixelCount] = 0
            pixelCount += 1
        rowCount += 1

    mat_plot.imsave("data/map-cyan-pixels.jpg", binaryImg, cmap = cm.gray)
    print("[Found all cyan pixels and saved binary image to data folder]")

    return binaryImg


def detect_connected_components(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

