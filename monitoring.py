# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API.

    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date


    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"

    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )

    res = requests.get(url)
    return res.json()


#IDEAS
    # call and retrieve list of groups of monitoring sites for user to select
    # call and retrieve list of monitoring sites for group for user to select
    # call and retrieve list of species for user to select

    # once all information is retrieved, user can select monitoring site and species
        #create different funcs for different options
            #pollutant value every hour for chosen dates
            #find more different options

    # create graphs with ❚ character

def callGroups(): #retrieves list of groups
    # TODO: documentation

    import requests

    url = "https://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json"

    res = requests.get(url).json()
    return res


def callSitesSpecies(groupName): #retrieves list of monitoring sites and species for group
    # TODO: documentation

    import requests

    url = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={groupName}/Json"

    res = requests.get(url).json()
    return res


import json
with open("output/data.json", "w") as file:
    json.dump(callGroups(), file, indent = 3)

# TODO: func -> display groups to choose

# TODO: func -> display sites in group to choose

# TODO: func -> display species for specific site

# TODO: func -> display data (bar chart) for pollutant level every hour depending on date




#EXAMPLE BAR CHART DISPLAY
str = "item1"
print("| " + "❚" * 21 + f" <- {str}")
print("| " + "❚" * 34 + " <- item2")
print("| " + "❚" * 16 + " <- item3")