# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import pandas
import json

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

    # TODO: rewrite to prevent / 0 when a whole day is No data
    i = 0
    means = []
    while i < len(siteData):
        temp = siteData[i:i+24]
        sum, count, mean = 0, 0, 0
        for dict in temp:
            if dict[pollutant] != "No data":
                sum += float(dict[pollutant])
                count += 1
        i += 24
        if count == 0:
            means.append("N/A")
        else:
            mean = sum / count
            means.append(mean)

    return means


def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here


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