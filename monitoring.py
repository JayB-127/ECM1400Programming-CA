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

    response= requests.get(url)
    return response.json()


def callGroups():
    """Creates a get request and returns data about the different groups available in the API.
    
    Returns:
        (JSON Obj) response: JSON object containing information on the different groups available."""

    import requests

    url = "https://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json"

    response = requests.get(url).json()
    return response


def callSitesSpecies(groupName):
    """Creates a get request and returns data about the different sites and species available in the API.
    
    Keyword arguments:
        (String) groupName: String representing the name of the group chosen by the user.

    Returns:
        (JSON Obj) response: JSON object containing information on the different sites and species available."""

    import requests

    url = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={groupName}/Json"

    response= requests.get(url).json()
    return response


def selectGroup():
    """Displays a list of the groups available, taking a user input for a certain group. The name of the chosen group is returned.
    
    Returns:
        (String) groupName[0]: String representing the group name chosen by the user.
    """

    data = callGroups()
    data = data["Groups"]["Group"] #retrieve list of dicts of information on each group

    print("--- Groups ---")
    count = 0
    for dictionary in data:
        print(str(count) + " - " + dictionary["@GroupName"])
        count += 1

    print("? - Main Menu")

    group = input("Select a group: ")

    if group == "?":
        return
    
    groupName = [data[i]["@GroupName"] for i in range(count) if group == str(i)] #list comprehension for finding group chosen
    print(f"[{groupName[0]} SELECTED]")
    return groupName[0]


def selectSite(groupName):
    """Displays a list of the sites available, taking a user input for a certain site. The code of the chosen site is returned.
    
    Keyword arguments:
        (String) groupName: String representing the name of the group chosen by the user.
        
    Returns:
        (String) siteCode[0]: String representing the code of the site chosen by the user.
        (String) siteCode: String representing the code of the site chosen by the user."""

    data = callSitesSpecies(groupName)
    data = data["Sites"]["Site"] #retrieve list of dicts of information on each site
    
    print("--- Monitoring Sites ---")
    print(type(data))
    if isinstance(data, list):
        if len(data) != 0:
            count = 0
            for dictionary in data:
                print(str(count) + " - " + dictionary["@SiteName"])
                count += 1
            print("? - Main Menu")
            site = input("Select a monitoring site: ")
            if site == "?":
                return
            siteCode = [data[i]["@SiteCode"] for i in range(count) if site == str(i)] #list comprehension for finding the site chosen
            print(f"[{siteCode[0]} SELECTED]")
            return siteCode[0]
        else:
            return
    elif isinstance(data, dict):
        print("0 - " + data["@SiteName"])
        print("? - Main Menu")
        site = input("Select a monitoring site: ")
        if site == "?":
            return
        elif site != "0":
            print("Invalid input. Try again.")
            return
        siteCode = data["@SiteCode"]
        print(f"[{siteCode} SELECTED]")
        return siteCode


def selectSpecies(groupName, siteCode):
    """Displays a list of the species available for a specific site, taking a user input for a certain species. The code of the species is returned.
    
    Keyword arguments:
        (String) groupName: String representing the name of the group chosen by the user.
        (String) siteCode: String representing the code of the site chosen by the user.
        
    Returns:
        (String) species[0]: String representing the code of the species chosen by the user.
        (String) species: String representing the code of the species chosen by the user."""

    data = callSitesSpecies(groupName)
    data = data["Sites"]["Site"]

    if isinstance(data, list):
        for item in data:
            if item["@SiteCode"] == siteCode:
                if isinstance(item["Species"], list):
                    if len(item["Species"]) != 0:
                        count = 0
                        for speciesDict in item["Species"]:
                            print(str(count) + " - " + speciesDict["@SpeciesDescription"])
                            count += 1
                        print("? - Main Menu")
                        speciesIndex = input("Select a species: ")
                        if speciesIndex == "?":
                            return
                        species = [item["Species"][i]["@SpeciesCode"] for i in range(count) if speciesIndex == str(i)]
                        print(f"[{species[0]} SELECTED]")
                        return species[0]
                    else:
                        return
                elif isinstance(item["Species"], dict):
                    print("0 - " + item["Species"]["@SpeciesDescription"])
                    print("? - Main Menu")
                    speciesIndex = input("Select a species: ")
                    if speciesIndex == "?":
                        return
                    elif speciesIndex != "0":
                        print("Invalid input. Try again.")
                        return
                    species = item["Species"]["@SpeciesCode"]
                    print(f"[{species} SELECTED]")
                    return species
    elif isinstance(data, dict):
        if isinstance(data["Species"], list):
            if len(data["Species"]) != 0:
                count = 0
                for speciesDict in data["Species"]:
                    print(str(count) + " - " + speciesDict["@SpeciesDescription"])
                    count += 1
                print("? - Main Menu")
                speciesIndex = input("Select a species: ")
                if speciesIndex == "?":
                    return
                species = [data["Species"][i]["@SpeciesCode"] for i in range(count) if speciesIndex == str(i)]
                print(f"[{species[0]} SELECTED]")
                return species[0]
            else:
                        return
        elif isinstance(data["Species"], dict):
            print("0 - " + data["Species"]["@SpeciesDescription"])
            print("? - Main Menu")
            speciesIndex = input("Select a species: ")
            if speciesIndex == "?":
                return
            elif speciesIndex != "0":
                print("Invalid input. Try again.")
                return
            species = data["Species"]["@SpeciesCode"]
            print(f"[{species} SELECTED]")
            return species


def displayHourlyData():
    """Allows the user to select a certain group, site and species, displaying live data for the specified group, site and species in a bar chart.
    An hourly average is also calculated and displayed."""

    import requests
    import datetime

    group = selectGroup()
    if group is None:
        return

    site = selectSite(group)
    if site is None:
        return

    species = selectSpecies(group, site)
    if species is None:
        return

    startDateInput = input("Enter a start date (type 'today' for current date): ")
    if startDateInput.lower() == "today" or startDateInput == str(datetime.date.today()):
        startDate = datetime.date.today()
        endDate = (datetime.datetime.strptime(str(startDate), "%Y-%m-%d") + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
    else:
        startDate = startDateInput
        endDateInput = input("Enter an end date (type 'today' for current date): ")
        if endDateInput == startDate:
            endDate = (datetime.datetime.strptime(str(startDate), "%Y-%m-%d") + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
        elif endDateInput.lower() == "today":
            endDate = datetime.date.today()
        else:
            endDate = endDateInput

    url = f"https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site}/SpeciesCode={species}/StartDate={startDate}/EndDate={endDate}/Json"

    response= requests.get(url).json()

    data = response["RawAQData"]["Data"]

    print(f"--- Hourly Data ({site}, {species}) ---")

    values = []
    for hour in data:
        hourTime = hour["@MeasurementDateGMT"]
        if hour["@Value"] == "":
            print(f"{hourTime} | -")
        else:
            value = float(hour["@Value"])
            values.append(value)
            if round(value) == 0:
                print(f"{hourTime} | ❚" + f" {value}")
            else:
                print(f"{hourTime} | " + "❚" * round(value) + f" {value}")

    print(f"--- Average Value ({site}, {species}) ---")

    from utils import meannvalue

    if len(values) != 0:
        mean = round(meannvalue(values), 2)
        print(f"Average value for {species} at {site} = {mean}")
    else:
        print("No data available for average to be calculated.")