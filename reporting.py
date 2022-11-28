# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import pandas
import numpy

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

    siteData = data[monitoring_station]

    i = 0
    means = []
    while i < len(siteData):
        day = siteData[i:i+24]
        sum, count, mean = 0, 0, 0
        for hour in day:
            if hour[pollutant] != "No data":
                sum += float(hour[pollutant])
                count += 1
        i += 24
        if count == 0:
            means.append("N/A")
        else:
            mean = sum / count
            means.append(mean)

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
    

daily_median(get_data(), "Marylebone Road", "no")


def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here


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