# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """Receives a list/array, returning the sum of the values in that sequence.

    Keyword arguments:
        values -- the list/array of values.
        
    Returns:
        sum -- the sum of all the values."""
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
        values -- the list/array of values.
        
    Returns:
        maxIndex -- the index of the maximum value."""
    maxIndex = 0
    max = values[0]
    i = 0
    while i < len(values):
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
        values -- the list/array of values.
        
    Returns:
        minIndex -- the index of the minimum value."""
    minIndex = 0
    min = values[0]
    i = 0
    while i < len(values):
        if type(values[i]) == int or type(values[i]) == float or type(values[i]) == complex: #TODO: better syntax than this
            if values[i] < min:
                minIndex = i
                min = values[i]
            i += 1
        else:
            raise Exception("All values in sequence must be numerical. Wrong data type given.")
    return minIndex


def meannvalue(values):
    """Receives a list/array, returning the arithmetic mean value in that sequence.
    
    Keyword arguments:
        values -- the list/array of values.
        
    Returns:
        mean -- the mean value."""    
    sum = 0
    for item in values:
        if type(item) == int or type(item) == float or type(item) == complex: #TODO: better syntax than this
            sum += item
        else:
            raise Exception("All values in sequence must be numerical. Wrong data type given.")
    mean = sum / len(values)
    return mean


def countvalue(values,x):
    #TODO: make x keyword argument new line in docstring
    """Receives a list/array values and a value x, returning the number of occurrences of the value x in that sequence.
    
    Keyword arguments:
        values -- the list/array of values.
        x -- the value to find in the sequence.
        
    Returns:
        occurences -- the amount of times x is present in the sequence."""
    occurences = 0
    for item in values:
        if item == x:
            occurences += 1
    return occurences