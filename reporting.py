# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

from pandas import read_csv
import numpy as np
from datetime import datetime
from csv import DictWriter

def get_data():
    """Reads all csv files and returns a dictionary containing three keys for each monitoring station.
    Each of the three keys is mapped a list of values which are dictionaries containing data, each for a specific hour.

    Returns:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station."""

    #read csv files into dataframes
    #convert the dataframes to a list of dictionaries
    hdataframe = read_csv("data\Pollution-London Harlington.csv")
    hdata = hdataframe.to_dict("records")

    mdataframe = read_csv("data\Pollution-London Marylebone Road.csv")
    mdata = mdataframe.to_dict("records")

    ndataframe = read_csv("data\Pollution-London N Kensington.csv")
    ndata = ndataframe.to_dict("records")

    #create a dictionary that maps the list of dictionaries for each monitoring station to a key
    data = {"Harlington" : hdata, "Marylebone Road" : mdata, "N Kensington" : ndata}

    return data


def daily_average(data, monitoring_station, pollutant):
    """Returns a list/array containing the daily averages for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (List/Array) means: List/Array containing 365 daily mean averages for a particular pollutant and monitoring station."""

    from utils import meannvalue

    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    i = 0
    means = []
    while i < len(stationData):
        values = []
        #retrieve dictionaries in lists of 24 every iteration. This is due to there being 24 hours each day
        day = stationData[i:i+24]
        #iterate through each dictionary (hour) in the list of 24 dictionaries
        for hour in day:
            if hour[pollutant] != "No data":
                values.append(float(hour[pollutant]))
        #increment i so that the dictionaries for the next day are retrieved
        i += 24
        
        if len(values) == 0:
            means.append("N/A")
        #calculate the mean on the list of values for that day, appending the result to the list/array of mean averages
        else:
            #use util.py function to calculate mean value
            means.append(meannvalue(values))

    return means


def daily_median(data, monitoring_station, pollutant):
    """Returns a list/array containing the daily median values for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (List/Array) medians: List/Array containing 365 daily median values for a particular pollutant and monitoring station."""

    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    i = 0
    medians = []
    while i < len(stationData):
        values = []
        #retrieve dictionaries in lists of 24 every iteration. This is due to there being 24 hours each day.
        day = stationData[i:i+24]
        #iterate through each dictionary (hour) in the list of 24 dictionaries
        for hour in day:
            if hour[pollutant] != "No data":
                values.append(float(hour[pollutant]))
        #increment i so that the dictionaries for the next day are retrieved
        i += 24

        #order the list of different values of pollutant for that day in ascending order
        values = np.sort(values)
        n = len(values)
        if n == 0:
            medians.append("N/A")
        #calculate median on the values depending on if there are an even or odd amount of values, appending the result to the list/array
        elif n % 2 == 0:
            n = int(n / 2)
            median = 0.5 * (values[n - 1] + values[n])
            medians.append(median)
        elif n % 2 != 0:
            n = int((n + 1) / 2)
            median = values[n-1]
            medians.append(median)

    return medians


def hourly_average(data, monitoring_station, pollutant):
    """Returns a list/array containing the hourly averages for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (List/Array) means: List/Array containing 24 hourly mean averages for a particular pollutant and monitoring station."""

    from utils import meannvalue
    
    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    means = []
    i = 1
    while i < 25:
        #set time to standard format, i representing the current hour. To start, i is set to 1 representing the time 01:00:00
        time = "%02d:00:00" %i
        values = []
        #iterate through each dictionary (hour) in the list of dictionaries
        for hour in stationData:
            if hour["time"] == time:
                if hour[pollutant] != "No data":
                    values.append(float(hour[pollutant]))
        #increment hour by one
        i += 1

        if len(values) == 0:
            means.append("N/A")
        else:
            #use util.py function to calculate mean value
            means.append(meannvalue(values))

    return means


def monthly_average(data, monitoring_station, pollutant):
    """Returns a list/array containing the monthly averages for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (List/Array) means: List/Array containing 12 monthly mean averages for a particular pollutant and monitoring station."""
    
    from utils import meannvalue

    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    means = []
    i = 1
    while i < 13:
        values = []
        #iterate through each dictionary (hour) in the list of dictionaries
        for hour in stationData:
            #convert string value of date in dictionary into a date object
            date = datetime.strptime(hour["date"], "%Y-%m-%d")
            #check if month part of the date value matches that of the current month
            if date.month == i:
                if hour[pollutant] != "No data":
                    values.append(float(hour[pollutant]))
        #increment month by one
        i += 1

        if len(values) == 0:
            means.append("N/A")
        else:
            #use util.py function to calculate mean value
            means.append(meannvalue(values))

    return means


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Returns the hour of the day with the highest pollutant level and its corresponding value for a particular pollutant and monitoring station
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) date: String representing a date chosen by the user, in the format YY:MM:DD
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (String) times[maxvalue(pollLevels)]: String representing the time at which the pollutant level is at its maximum on the date given.
        (Float) pollLevels[maxvalue(pollLevels)]: Float representing the maximum pollutant level on the date given."""

    from utils import maxvalue

    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    times = []
    pollLevels = []
    #iterate through each dictionary (hour) in the list of dictionaries
    for hour in stationData:
        if hour["date"] == date:
            if hour[pollutant] != "No data":
                times.append(hour["time"])
                pollLevels.append(float(hour[pollutant]))

    if len(times) == 0:
        return "No data for this day. Try another date."
    else:
        #the return value of maxvalue() will be the index at which the maximum pollutant level is in the list pollLevels
        #since the order of index in times and pollLevels is the same, the time and pollutant value are at the same index
        return times[maxvalue(pollLevels)], pollLevels[maxvalue(pollLevels)]


def count_missing_data(data, monitoring_station, pollutant):
    """Returns the number of "No data" entries there are in the data for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (Int) count: Integer representing the amount of occurences of "No data" entries in the data."""

    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    count = 0
    #iterate through each dictionary (hour) in the list of dictionaries
    for hour in stationData:
        if hour[pollutant] == "No data":
            #increment count by one everytime a "No data" entry is found
            count += 1

    return count


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Returns a copy of the data with the missing values replaced by the value in the parameter new_value for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) new_value: String representing the value that will replace all instances of "No data" in the data.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (List) stationData: List of dictionaries of data for the specified monitoring station where 'No data' entries for a particular pollutant are replaced by value of new_value parameter.
    """

    #retrieve a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    #loop through each hour, updating any 'No data' values to that of the new_value parameter
    for hour in stationData:
        if hour[pollutant] == "No data":
            hour.update({pollutant:new_value})

    #create (or overwrite) a csv file, writing the new modified data to it
    filename = f"output/{monitoring_station}, {pollutant} - fill_missing_data.csv"
    with open(filename, "w", newline="") as f:
        #create dictionary writer
        writer = DictWriter(f, stationData[0].keys())
        #write key names at the top of the csv file
        writer.writeheader()
        #write values into file
        writer.writerows(stationData)

    #print confirmation of creating new file to user
    print(f"[All 'No data' entries replaced by '{new_value}' and file copied to output folder]")

    return stationData