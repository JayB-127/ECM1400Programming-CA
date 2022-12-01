# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

from pandas import read_csv
import numpy
from datetime import datetime

def get_data():
    """Reads all csv files and returns a dictionary containing three keys for each monitoring station.
    Each of the three keys is mapped a list of values which are dictionaries containing data, each for a specific hour.

    Returns:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station."""

    #reads csv files into dataframes, then converts the dataframes to a list of dictionaries
    hdataframe = read_csv("data\Pollution-London Harlington.csv")
    hdata = hdataframe.to_dict("records")

    mdataframe = read_csv("data\Pollution-London Marylebone Road.csv")
    mdata = mdataframe.to_dict("records")

    ndataframe = read_csv("data\Pollution-London N Kensington.csv")
    ndata = ndataframe.to_dict("records")

    #creates a dictionary that maps the list of dictionaries for each monitoring station to a key
    data = {"Harlington" : hdata, "Marylebone Road" : mdata, "N Kensington" : ndata}

    return data


def daily_average(data, monitoring_station, pollutant):
    """Returns a list/array containing the daily averages for a particular pollutant and monitoring station.
    
    Keyword arguments:
        (Dict) data: Dictionary containing three keys, each being mapped to a list of dictionaries of data for a monitoring station.
        (String) monitoring_station: String representing the monitoring station chosen by the user.
        (String) pollutant: String representing the pollutant chosen by the user.
        
    Returns:
        (List/Array) means: List/Array containing 365 daily mean averages for a particular pollutant and monitoring station"""

    from utils import meannvalue

    #retrieves a list of dictionaries of data for the specified monitoring station
    stationData = data[monitoring_station]

    i = 0
    means = []
    #loops until end of list of dictionaries
    while i < len(stationData):
        #retrieve dictionaries in lists of 24 every iteration. This is due to there being 24 hours each day
        day = stationData[i:i+24]
        values = []
        #iterate through each dictionary (hour) in the list of 24 dictionaries
        for hour in day:
            #append the float value of the pollutant level, if there is data present (not 'No data')
            if hour[pollutant] != "No data":
                values.append(float(hour[pollutant]))
        i += 24
        
        #if there are no values to calculate the mean of, the average will be N/A
        if len(values) == 0:
            means.append("N/A")
        #calculate the mean on the list of values for that day, appending the result to the list/array of mean averages
        else:
            means.append(meannvalue(values))

    return means


def daily_median(data, monitoring_station, pollutant):
    # TODO: documentation

    stationData = data[monitoring_station]

    i = 0
    medians = []
    while i < len(stationData):
        values = []
        day = stationData[i:i+24]
        for hour in day:
            if hour[pollutant] != "No data":
                values.append(float(hour[pollutant]))
        i += 24

        values = numpy.sort(values)
        n = len(values)
        if n == 0:
            medians.append("N/A")
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
    # TODO: documentation

    from utils import meannvalue
    
    stationData = data[monitoring_station]

    means = []
    i = 1
    while i < 25:
        time = "%02d:00:00" %i
        values = []
        for hour in stationData:
            if hour["time"] == time:
                if hour[pollutant] != "No data":
                    values.append(float(hour[pollutant]))
        i += 1 #increments hour by one

        if len(values) == 0:
            means.append("N/A")
        else:
            means.append(meannvalue(values))

    return means
  

def monthly_average(data, monitoring_station, pollutant):
    # TODO: documentation
    
    from utils import meannvalue

    stationData = data[monitoring_station]

    means = []
    i = 1
    while i < 13:
        values = []
        for hour in stationData:
            date = datetime.strptime(hour["date"], "%Y-%m-%d") #converts string into date obj
            if date.month == i:
                if hour[pollutant] != "No data":
                    values.append(float(hour[pollutant]))
        i += 1 #increments month by one

        if len(values) == 0:
            means.append("N/A")
        else:
            means.append(meannvalue(values))

    return means


def peak_hour_date(data, date, monitoring_station, pollutant):
    # TODO: documentation

    from utils import maxvalue

    stationData = data[monitoring_station]

    times = []
    pollLevels = []
    for hour in stationData:
        if hour["date"] == date:
            if hour[pollutant] != "No data":
                times.append(hour["time"])
                pollLevels.append(float(hour[pollutant]))

    if len(times) == 0:
        return "No data for this day. Try another date."
    else:
        return times[maxvalue(pollLevels)], pollLevels[maxvalue(pollLevels)]


def count_missing_data(data, monitoring_station, pollutant):
    # TODO: documentation

    stationData = data[monitoring_station]

    count = 0
    for hour in stationData:
        if hour[pollutant] == "No data":
            count += 1

    return count


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    # TODO: documentation
    
    stationData = data[monitoring_station]

    for hour in stationData:
        if hour[pollutant] == "No data":
            pass