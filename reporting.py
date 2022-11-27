# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy
from datetime import date, time

def get_data():
    # TODO: filename depends on monitoring site parsed into function
    filename = "data\Pollution-London Harlington.csv"
    # TODO: returns 2d array of csv file for that monitoring site
    array = numpy.loadtxt(
        filename,
        dtype = {
            "columns": ("date", "time", "no", "pm10", "pm25"),
            "formats": (date, time, float, float, float)},
        skiprows = 1,
        delimiter = ",",
        max_rows = 3)
    print(array)

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
