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
    for row in rgb_img: #for each row
        pixelCount = 0
        for pixel in row: #for each pixel in row
            if pixel[0] < lowerThresh and pixel[1] > upperThresh and pixel[2] > upperThresh:
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
    # TODO: documentation
    # TODO: explain how algorithm was improved and modified in documentation (switched if statement conditions for faster performance)

    colour = args[0]
    if colour == "red":
        img = find_red_pixels("data/map.png", upper_threshold = 100, lower_threshold = 50)
    elif colour == "cyan":
        img = find_cyan_pixels("data/map.png", upper_threshold = 100, lower_threshold = 50)

    mark = np.zeros([len(img), len(img[0])], dtype = int)

    queue = np.zeros(len(img) * len(img[0]), dtype=int) #set queue size to amount of pixels in img (max value it will need to be)
    fpoint = 0 #front pointer for queue
    bpoint = 0 #back pointer for queue

    rowCount = 0
    for row in img:
        pixelCount = 0
        for pixel in row:
            if pixel == 1 and mark[rowCount][pixelCount] == 0: #pavement pixel and unvisited
                pass
            pixelCount += 1
        rowCount += 1

detect_connected_components("cyan")

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here