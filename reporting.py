# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy

def get_data(monitoring_station):
    # TODO: documentation

    #create filename specific to each monitoring station selected in main menu
    filename = "data\Pollution-London " + monitoring_station + ".csv"
    #create a 2d array with the data from the csv file, removing the first row
    csv = numpy.genfromtxt(filename, delimiter=",", dtype=None).astype("U13")
    data = numpy.delete(csv, 0, 0)
    return data


def daily_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    # USE UTIL FUNCTIONS


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