# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy
from datetime import date, time

def get_data():
    filename = "data\Pollution-London Harlington.csv"
    # TODO: returns 2d array of csv file for that monitoring station
    data = numpy.loadtxt(
        filename,
        dtype = {
            "names": ("date", "time", "no", "pm10", "pm25"),
            "formats": (date, time, float, float, float)},
        skiprows = 1,
        delimiter = ",")
    print(data)

get_data()

def daily_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here

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
