# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import pandas
import numpy
from datetime import datetime, timedelta

def get_data():
    # TODO: documentation

    filename = "data\Pollution-London Harlington.csv"
    hdataframe = pandas.read_csv(filename)
    hdata = hdataframe.to_dict("records")

    filename = "data\Pollution-London Marylebone Road.csv"
    mdataframe = pandas.read_csv(filename)
    mdata = mdataframe.to_dict("records")

    filename = "data\Pollution-London N Kensington.csv"
    ndataframe = pandas.read_csv(filename)
    ndata = ndataframe.to_dict("records")

    data = {"Harlington" : hdata, "Marylebone Road" : mdata, "N Kensington" : ndata}

    return data


def daily_average(data, monitoring_station, pollutant):
    # TODO: documentation

    from utils import meannvalue

    siteData = data[monitoring_station]

    i = 0
    means = []
    while i < len(siteData):
        day = siteData[i:i+24]
        values = []
        for hour in day:
            if hour[pollutant] != "No data":
                values.append(float(hour[pollutant]))
        i += 24
        
        if len(values) == 0:
            means.append("N/A")
        else:
            means.append(meannvalue(values))

    return means


def daily_median(data, monitoring_station, pollutant):
    # TODO: documentation

    siteData = data[monitoring_station]

    i = 0
    medians = []
    while i < len(siteData):
        values = []
        day = siteData[i:i+24]
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
    
    siteData = data[monitoring_station]

    means = []
    i = 1
    while i < 25:
        time = "%02d:00:00" %i
        values = []
        for hour in siteData:
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
    """Your documentation goes here"""
    
    ## Your code goes here


def peak_hour_date(data, date, monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here


def count_missing_data(data,  monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here


def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here