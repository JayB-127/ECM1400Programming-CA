# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """Receives a list/array and returns the sum of the values in that sequence.

    Keyword arguments:
        values -- the list/array of values that are to be summed"""
    sum = 0
    for item in values:
        if type(item) != int:
            raise Exception("All values in sequence must be numerical. Wrong data type given.")
        else:
            sum += item
    return sum

array = [3, 2, 4, 65, "asd"]
print(sumvalues(array))

def maxvalue(values):
    """Your documentation goes here"""    
    ## Your code goes here


def minvalue(values):
    """Your documentation goes here"""    
    ## Your code goes here


def meannvalue(values):
    """Your documentation goes here"""    
    ## Your code goes here


def countvalue(values,xw):
    """Your documentation goes here"""    
    ## Your code goes here
