# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """Receives a list/array, returning the sum of the values in that sequence.

    Keyword arguments:
        values -- the list/array of values"""
    sum = 0
    for item in values:
        if type(item) == int or type(item) == float or type(item) == complex: #TODO: better syntax than this
            sum += item
        else:
            raise Exception("All values in sequence must be numerical. Wrong data type given.")
    return sum


def maxvalue(values):
    """Receives a list/array, returning the index of the maximum value in that sequence.
    
    Keyword arguments:
        values -- the list/array of values"""
    maxIndex = 0
    max = 0
    i = 0
    while i < len(values):
        #TODO: raise exception for nonnumerical
        if type(values[i]) == int or type(values[i]) == float or type(values[i]) == complex: #TODO: better syntax than this
            if values[i] > max:
                maxIndex = i
                max = values[i]
            i += 1
        else:
            raise Exception("All values in sequence must be numerical. Wrong data type given.")
    return maxIndex


def minvalue(values):
    """Receives a list/array, returning the index of the minimum value in that sequence.
    
    Keyword arguments:
        values -- the list/array of values"""
    ## Your code goes here


def meannvalue(values):
    """Receives a list/array, returning the arithmetic mean value in that sequence.
    
    Keyword arguments:
        values -- the list/array of values"""    
    ## Your code goes here


def countvalue(values,x):
    """documentation here"""    
    ## Your code goes here
