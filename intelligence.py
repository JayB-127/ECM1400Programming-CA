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

    mat_plot.imsave("output/map-red-pixels.jpg", binaryImg, cmap = cm.gray)
    print("[Found all red pixels. Saved binary image to output folder]")

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

    mat_plot.imsave("output/map-cyan-pixels.jpg", binaryImg, cmap = cm.gray)
    print("[Found all cyan pixels. Saved binary image to output folder]")

    return binaryImg


def detect_connected_components(*args,**kwargs):
    # TODO: documentation
    # TODO: explain how algorithm was improved and modified in documentation

    img = args[0]

    mark = np.zeros([len(img), len(img[0])], dtype = int)

    queue = np.zeros([len(img) * len(img[0]), 2], dtype = int) #set queue size to amount of pixels in img (max value it will need to be)
    fpointer = 0 #front pointer for queue
    bpointer = 0 #back pointer for queue

    visitedDigit = 1
    components = []

    rowCount = 0
    for row in img:
        pixelCount = 0
        for pixel in row:
            #??? componentSize = 0 ???
            componentSize = 0
            if pixel == 1 and mark[rowCount][pixelCount] == 0: #unvisited and pavement pixel
                #set mark[rowCount][pixelCount] as visited digit
                mark[rowCount][pixelCount] = visitedDigit
                #add pixel position to queue
                queue[bpointer] = [rowCount, pixelCount]
                bpointer += 1
                #while queue not empty
                while queue[fpointer].any() != 0:
                    #remove first item from queue and set as current pixel
                    currentRow, currentColumn = queue[fpointer]
                    fpointer += 1
                    #for each 8-neighbour of current pixel
                    for y in range(-1, 2):
                        for x in range(-1, 2):
                            #check index out of range
                            if (currentRow + y) < 0 or (currentRow + y) > (len(img) - 1) or (currentColumn + x) < 0 or (currentColumn + x) > (len(img[0]) - 1):
                                continue
                            elif y == 0 and x == 0: #current pixel
                                continue
                            else:
                                #if unvisited and pavement pixel
                                if mark[currentRow + y][currentColumn + x] == 0 and img[currentRow + y][currentColumn + x] == 1:
                                    mark[currentRow + y][currentColumn + x] = visitedDigit #set pixel as visited
                                    queue[bpointer] = [currentRow + y, currentColumn + x] #add pixel to queue
                                    bpointer += 1

                    #??? increment componentSize by 1 ???
                    componentSize += 1

                #increment visited digit by one since connected component is finished
                visitedDigit += 1
                #??? append "Connected Component {visited digit}, number of pixels = {componentSize}" to array???
                components.append(f"Connected Component {visitedDigit - 1}, number of pixels = {componentSize}")
                pass
            pixelCount += 1
        rowCount += 1

    #write components array to file
    with open("output/cc-output-2a.txt", "w") as file:
        for line in components:
            file.write(line + "\n")
        file.write(f"Total number of connected components = {visitedDigit - 1}")

    print(f"[Detected all {visitedDigit - 1} connected components. Saved .txt file to output folder]")

    return mark


def detect_connected_components_sorted(*args,**kwargs):
    # TODO: documentation

    mark = args[0]

    componentsDict = {}
    #for row in mark
    for row in mark:
        #for pixel in row
        for pixel in row:
            #if pixel != 0:
            if pixel != 0:
                if pixel in componentsDict:
                    componentsDict[pixel] += 1
                else:
                    componentsDict.update({pixel:1})

    items = []
    for i in componentsDict.keys():
        items.append([i, componentsDict[i]])

    bubble2d(items) #sorted in descending order of pixel count (component size)

    with open("output/cc-output-2b.txt", "w") as file:
        for pair in items:
            str = f"Connected Component {pair[0]}, number of pixels = {pair[1]}\n"
            file.write(str)
        file.write(f"Total number of connected components = {items[0][0]}")

    #obtain two largest pairs from items
    #for every pixel in mark
        #if pixel is connected component number
            #set pixel as 1
        #else
            #set pixel as 0
    #mat_plot.imsave("output/cc-top-2b.jpg", binaryImg, cmap = cm.gray)
    # TODO: above


def bubble2d(items):

    swap = False
    for i in range(len(items) - 1, 0, -1):
        for j in range(len(items) - 1, len(items) - 1 - i, -1):
            if items[j][1] > items[j - 1][1]:
                items[j - 1], items[j] = items[j], items[j - 1]
                swap = True

            if swap == False:
                return

    return items