# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy as np
from matplotlib import pyplot as mat_plot
from matplotlib import cm


def find_red_pixels(map_filename, upper_threshold = 100, lower_threshold = 50):
    """Reads an rgb image and returns a 2D numpy array representing a binary image of all red pixels in the image.
    A pixel being red is based upon rgb thresholds.

    Keyword arguments:
        (String) map_filename: String representing the image file to be read.
        (Int) upper_threshold: Upper rgb threshold to determine pixel colour. It is given a default value of 100.
        (Int) lower_threshold: Lower rgb threshold to determine pixel colour. It is given a default value of 50.
    
    Returns:
        (NDarray) binaryImg: 2D ndarray representing the binary image."""

    rgb_img = mat_plot.imread(map_filename)
    rgb_img *= 255 #scale rgb values

    height = len(rgb_img)
    width = len(rgb_img[0])
    #2d numpy array size of map img
    binaryImg = np.zeros([height, width], dtype = int)
    
    #starting top left, checking each pixel in rgb image
    rowCount = 0
    for row in rgb_img:
        pixelCount = 0
        for pixel in row:
            #check if pixel is classified as red within the threshold values
            if pixel[0] > upper_threshold and pixel[1] < lower_threshold and pixel[2] < lower_threshold:
                #set pixel in binary image array to white
                binaryImg[rowCount][pixelCount] = 1
            else:
                #set pixel in binary image array to black
                binaryImg[rowCount][pixelCount] = 0
            pixelCount += 1
        rowCount += 1

    #create binary image from array
    mat_plot.imsave("output/map-red-pixels.jpg", binaryImg, cmap = cm.gray)
    print("[Found all red pixels. Saved binary image to output folder]")

    return binaryImg


def find_cyan_pixels(map_filename, upper_threshold = 100, lower_threshold = 50):
    """Reads an rgb image and returns a 2D numpy array representing a binary image of all cyan pixels in the image.
    A pixel being cyan is based upon rgb thresholds.

    Keyword arguments:
        (String) map_filename: String representing the image file to be read.
        (Int) upper_threshold: Upper rgb threshold to determine pixel colour. It is given a default value of 100.
        (Int) lower_threshold: Lower rgb threshold to determine pixel colour. It is given a default value of 50.
    
    Returns:
        (NDarray) binaryImg: 2D ndarray representing the binary image."""

    rgb_img = mat_plot.imread(map_filename)
    rgb_img *= 255 #scale rgb values

    height = len(rgb_img)
    width = len(rgb_img[0])
    #2d numpy array size of map img
    binaryImg = np.zeros([height, width], dtype = int)

    #starting top left, checking each pixel in rgb image
    rowCount = 0
    for row in rgb_img:
        pixelCount = 0
        for pixel in row:
            #check if pixel is classified as cyan within the threshold values
            if pixel[0] < lower_threshold and pixel[1] > upper_threshold and pixel[2] > upper_threshold:
                #set pixel in binary image array to white
                binaryImg[rowCount][pixelCount] = 1
            else:
                #set pixel in binary image array to black
                binaryImg[rowCount][pixelCount] = 0
            pixelCount += 1
        rowCount += 1

    #create binary image from array
    mat_plot.imsave("output/map-cyan-pixels.jpg", binaryImg, cmap = cm.gray)
    print("[Found all cyan pixels. Saved binary image to output folder]")

    return binaryImg


def detect_connected_components(IMG):
    """Reads a binary image and returns an array containing positional information on each connected component.
    The number of pixels inside each connected component is written to a .txt file.
    
    Keyword arguments:
        (NDarray) IMG: 2D ndarray representing the binary image.
    
    Returns:
        (NDarray) mark: 2D ndarray containing positional information on each connected component.
    
    Algorithm Improvements/Modifications:
        The first modification is when setting the position in mark as visited.
        Instead of setting it to the same value each time, the value is incremented for every different connected component.
        This means that it is clear which connected component is which when reading mark.
        
        In addition, when looking at the 8-neighbours around the current pixel, firstly the indexes of the pixels around are checked to ensure that they fit within the bounds of the 2d array.
        If they do not fit within the bounds then they are not checked as a pavement pixel.
        This means that errors do not occur when checking the 8-neighbour pixels.

        Another modification to the algorithm is that the size of each connected component is tracked as they are discovered.
        This prevents the mark array having to be searched again afterwards since the information of component size has already been calculated.
        
        The final improvement to the algorithm is that the information about the connected component to be displayed to the .txt file can be immediately be appended to the list that contains all the information.
        This prevents another search through mark, significantly reducing the execution time of the program.
        The data in the list can then be easily written to the .txt file."""

    #empty 2d array, size of binary image to mark if pixels have been visited or not
    mark = np.zeros([len(IMG), len(IMG[0])], dtype = int)

    #2d array for queue, size of binary image to allow for max queue
    queue = np.zeros([len(IMG) * len(IMG[0]), 2], dtype = int)
    fpointer = 0 #front pointer
    bpointer = 0 #back pointer

    visitedDigit = 1
    components = [] #array to store all component information

    #starting from top left, checking each pixel in binary image
    rowCount = 0
    for row in IMG:
        pixelCount = 0
        for pixel in row:
            componentSize = 0
            #check if pixel is a pavement pixel and unvisited
            if pixel == 1 and mark[rowCount][pixelCount] == 0:
                #set pixel as visited
                mark[rowCount][pixelCount] = visitedDigit
                #add position of pixel to queue
                queue[bpointer] = [rowCount, pixelCount]
                bpointer += 1
                #while queue is not empty
                while queue[fpointer].any() != 0:
                    currentRow, currentColumn = queue[fpointer]
                    fpointer += 1
                    #for each 8-neighbour of current pixel
                    for y in range(-1, 2):
                        for x in range(-1, 2):
                            #if index out of range
                            if (currentRow + y) < 0 or (currentRow + y) > (len(IMG) - 1) or (currentColumn + x) < 0 or (currentColumn + x) > (len(IMG[0]) - 1):
                                continue
                            #if index in range
                            else:
                                #check if pixel is unvisited and a pavement pixel
                                if mark[currentRow + y][currentColumn + x] == 0 and IMG[currentRow + y][currentColumn + x] == 1:
                                    #set pixel as visited
                                    mark[currentRow + y][currentColumn + x] = visitedDigit
                                    #add position of pixel to queue
                                    queue[bpointer] = [currentRow + y, currentColumn + x]
                                    bpointer += 1
                    componentSize += 1
                #component completed so increment visitedDigit to represent new component
                visitedDigit += 1
                #add component information to array
                components.append(f"Connected Component {visitedDigit - 1}, number of pixels = {componentSize}")
            pixelCount += 1
        rowCount += 1

    #write all component information to .txt file
    with open("output/cc-output-2a.txt", "w") as file:
        for line in components:
            file.write(line + "\n")
        file.write(f"Total number of connected components = {visitedDigit - 1}")

    print(f"[Detected all {visitedDigit - 1} connected components. Saved .txt file to output folder]")

    return mark


def detect_connected_components_sorted(MARK):
    """Iterates through a 2D ndarray containing positional information on each connected component, writing information on all connected components in a .txt file in descending order of size.
    It also saves the two largest connected components to a .jpg file as a binary image.
    
    Keyword arguments:
        (NDarray) MARK: 2D ndarray containing positional information on each connected component."""

    componentsDict = {} #dictionary to store all component information
    
    #starting from top left, checking each pixel in MARK
    for row in MARK:
        for pixel in row:
            #if pixel has been visited (must be component)
            if pixel != 0:
                #if pixel is in dictionary, increment its size value by 1
                if pixel in componentsDict:
                    componentsDict[pixel] += 1
                #if pixel is not in dictionary, add it and give it a size value of 1
                else:
                    componentsDict.update({pixel:1})

    items = [] #array to store component information
    #add all data from dictionary into 2d array
    for i in componentsDict.keys():
        items.append([i, componentsDict[i]])

    #use bubble sort to order components in descending order of component size
    bubble2d(items)

    #write all component information to .txt file
    with open("output/cc-output-2b.txt", "w") as file:
        count = 0
        for pair in items:
            str = f"Connected Component {pair[0]}, number of pixels = {pair[1]}\n"
            file.write(str)
            count += 1 #count number of connected components
        file.write(f"Total number of connected components = {count}")

    largest1 = items[0][0] #1st largest component
    largest2 = items[1][0] #2nd largest component

    #starting from top left, checking each pixel in MARK
    rowCount = 0
    for row in MARK:
        pixelCount = 0
        for pixel in row:
            #if pixel is from either 1st or 2nd largest components
            if pixel == largest1 or pixel == largest2:
                #set pixel to 1
                MARK[rowCount][pixelCount] = 1
            #if pixel is from any other component or none at all
            else:
                #set pixel to 0
                MARK[rowCount][pixelCount] = 0
            pixelCount += 1
        rowCount += 1

    #create binary image from MARK array
    mat_plot.imsave("output/cc-top-2b.jpg", MARK, cmap = cm.gray)


def bubble2d(items):
    """Orders a 2D array of shape (x, 2), where x is any value, in descending order according to each second index.
    It sorts the data by using a bubble sort.
    
    Keyword arguments:
        (2Darray) items: The array of items to be sorted.
        
    Returns:
        (2Darray) items: The array of items after being sorted in descending order according to each second index."""

    swap = False #no swaps occured and we assume the values are sorted
    #for each item in list of values
    for i in range(len(items) - 1, 0, -1):
        #for each item that hasn't already been sorted
        for j in range(len(items) - 1, len(items) - 1 - i, -1):
            #if current item is larger than the one at the index before
            if items[j][1] > items[j - 1][1]:
                #swap items
                items[j - 1], items[j] = items[j], items[j - 1]
                swap = True #a swap has occurred

            #if there were no swaps in that iteration, the values must be sorted
            if swap == False:
                return

    return items