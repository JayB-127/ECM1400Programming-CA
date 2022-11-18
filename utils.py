# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """Receives a list/array, returning the sum of the values in that sequence.

    Keyword arguments:
        values -- the list/array of values"""
    sum = 0
    for item in values:
        if type(item) != int:
            raise Exception("All values in sequence must be numerical. Wrong data type given.")
        else:
            sum += item
    return sum


def maxvalue(values):
    """Receives a list/array, returning the index of the maximum value in that sequence.
    
    Keyword arguments:
        values -- the list/array of values"""    
    ## Your code goes here


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
