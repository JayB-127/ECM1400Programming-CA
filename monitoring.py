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

    #create url to retrieve data from
    url = "https://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json"

    #send get request
    response = requests.get(url).json()
    return response


def callSitesSpecies(groupName):
    """Creates a get request and returns data about the different sites and species available in the API.
    
    Keyword arguments:
        (String) groupName: String representing the name of the group chosen by the user.

    Returns:
        (JSON Obj) response: JSON object containing information on the different sites and species available."""

    import requests

    #create url to retrieve data from
    url = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={groupName}/Json"

    #send get request
    response= requests.get(url).json()
    return response


def selectGroup():
    """Displays a list of the groups available, taking a user input for a certain group. The name of the chosen group is returned.
    
    Returns:
        (String) groupName[0]: String representing the group name chosen by the user.
    """

    data = callGroups()
    #isolate only necessary data
    data = data["Groups"]["Group"]

    print("--- Groups ---")
    count = 0
    #for each group
    for dictionary in data:
        #display the group name with a number for the user to select
        print(str(count) + " - " + dictionary["@GroupName"])
        count += 1

    print("? - Main Menu")
    group = input("Select a group: ")
    if group == "?":
        return
    #check for invalid input
    valid = False
    for x in range(count):
        if group == str(x):
            valid = True
            break
    if valid == False:
        print("Invalid input. Try again.")
        return
    
    #find group chosen and return group name
    groupName = [data[i]["@GroupName"] for i in range(count) if group == str(i)]
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
    #isolate only necessary data
    data = data["Sites"]["Site"]
    
    print("--- Monitoring Sites ---")
    #check if there is one (dict) or more (list) sites for the group
    if isinstance(data, list):
        if len(data) != 0:
            count = 0
            #for each site
            for dictionary in data:
                #display the site name with a number for the user to select
                print(str(count) + " - " + dictionary["@SiteName"])
                count += 1
            print("? - Main Menu")
            site = input("Select a monitoring site: ")
            if site == "?":
                return
            #check invalid input
            valid = False
            for x in range(count):
                if site == str(x):
                    valid = True
                    break
            if valid == False:
                print("Invalid input. Try again.")
                return
            #find site chosen and return site code
            siteCode = [data[i]["@SiteCode"] for i in range(count) if site == str(i)] #list comprehension for finding the site chosen
            print(f"[{siteCode[0]} SELECTED]")
            return siteCode[0]
        else:
            return
    #check if there is one (dict) or more (list) sites for the group
    elif isinstance(data, dict):
        #display the site name with a number for the user to select
        print("0 - " + data["@SiteName"])
        print("? - Main Menu")
        site = input("Select a monitoring site: ")
        if site == "?":
            return
        elif site != "0":
            print("Invalid input. Try again.")
            return
        #find site chosen and return site code
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
    #isolate only necessary data
    data = data["Sites"]["Site"]

    #check if there is one (dict) or more (list) sites for the group
    if isinstance(data, list):
        #for each species
        for item in data:
            if item["@SiteCode"] == siteCode:
                #check if there is one(dict) or more (list) species for the site
                if isinstance(item["Species"], list):
                    if len(item["Species"]) != 0:
                        count = 0
                        #for each species
                        for speciesDict in item["Species"]:
                            #display the species name with a number for the user to select
                            print(str(count) + " - " + speciesDict["@SpeciesDescription"])
                            count += 1
                        print("? - Main Menu")
                        speciesIndex = input("Select a species: ")
                        if speciesIndex == "?":
                            return
                        #check for invalid input
                        valid = False
                        for x in range(count):
                            if speciesIndex == str(x):
                                valid = True
                                break
                        if valid == False:
                            print("Invalid input. Try again.")
                            return
                        #find species chosen and return species code
                        species = [item["Species"][i]["@SpeciesCode"] for i in range(count) if speciesIndex == str(i)]
                        print(f"[{species[0]} SELECTED]")
                        return species[0]
                    else:
                        return
                #check if there is one(dict) or more (list) species for the site
                elif isinstance(item["Species"], dict):
                    #display the species name with a number for the user to select
                    print("0 - " + item["Species"]["@SpeciesDescription"])
                    print("? - Main Menu")
                    speciesIndex = input("Select a species: ")
                    if speciesIndex == "?":
                        return
                    elif speciesIndex != "0":
                        print("Invalid input. Try again.")
                        return
                    #find species chosen and return species code
                    species = item["Species"]["@SpeciesCode"]
                    print(f"[{species} SELECTED]")
                    return species
    #check if there is one (dict) or more (list) sites for the group
    elif isinstance(data, dict):
        #check if there is one(dict) or more (list) species for the site
        if isinstance(data["Species"], list):
            if len(data["Species"]) != 0:
                count = 0
                #for each species
                for speciesDict in data["Species"]:
                    #display the species name with a number for the user to select
                    print(str(count) + " - " + speciesDict["@SpeciesDescription"])
                    count += 1
                print("? - Main Menu")
                speciesIndex = input("Select a species: ")
                if speciesIndex == "?":
                    return
                #check for invalid input
                valid = False
                for x in range(count):
                    if speciesIndex == str(x):
                        valid = True
                        break
                if valid == False:
                    print("Invalid input. Try again.")
                    return
                #find species chosen and return species code
                species = [data["Species"][i]["@SpeciesCode"] for i in range(count) if speciesIndex == str(i)]
                print(f"[{species[0]} SELECTED]")
                return species[0]
            else:
                return
        #check if there is one(dict) or more (list) species for the site
        elif isinstance(data["Species"], dict):
            #display the species name with a number for the user to select
            print("0 - " + data["Species"]["@SpeciesDescription"])
            print("? - Main Menu")
            speciesIndex = input("Select a species: ")
            if speciesIndex == "?":
                return
            elif speciesIndex != "0":
                print("Invalid input. Try again.")
                return
            #find species chosen and return species code
            species = data["Species"]["@SpeciesCode"]
            print(f"[{species} SELECTED]")
            return species


def displayHourlyData():
    """Allows the user to select a certain group, site and species, displaying live data for the specified group, site and species in a bar chart.
    An hourly average is also calculated and displayed."""

    import requests
    import datetime

    #get group chosen by user
    group = selectGroup()
    if group is None:
        return

    #get site chosen by user
    site = selectSite(group)
    if site is None:
        return

    #get species chosen by user
    species = selectSpecies(group, site)
    if species is None:
        return

    #get user input for start data
    startDateInput = input("Enter a start date (type 'today' for current date) in format YYYY-MM-DD: ")

    #check start date entered is correct format
    try:
        datetime.datetime.strptime(startDateInput, '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return

    #if start date is set to current date
    if startDateInput.lower() == "today" or startDateInput == str(datetime.date.today()):
        startDate = datetime.date.today()
        #set end date to one more than start data
        endDate = (datetime.datetime.strptime(str(startDate), "%Y-%m-%d") + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
    else:
        startDate = startDateInput
        endDateInput = input("Enter an end date (type 'today' for current date) in format YYYY-MM-DD: ")
        #check end date entered is correct format
        try:
            datetime.datetime.strptime(endDateInput, '%Y-%m-%d')
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            return
        #if start date and end data are chosen to be the same
        if endDateInput == startDate:
            #set end date to one more than start date
            endDate = (datetime.datetime.strptime(str(startDate), "%Y-%m-%d") + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
        #if end date is set to current date
        elif endDateInput.lower() == "today":
            endDate = datetime.date.today()
        #if end date is before start date
        elif endDateInput < startDate:
            print("End date cannot be before start date. Try again.")
            return
        else:
            endDate = endDateInput

    #create url to retrieve date from
    url = f"https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site}/SpeciesCode={species}/StartDate={startDate}/EndDate={endDate}/Json"

    #send get request
    response = requests.get(url).json()

    #isolate only necessary data
    data = response["RawAQData"]["Data"]

    print(f"--- Hourly Data ({site}, {species}) ---")

    values = []
    #for each hour between dates chosen
    for hour in data:
        hourTime = hour["@MeasurementDateGMT"]
        #if there is no data for that hour
        if hour["@Value"] == "":
            print(f"{hourTime} | -")
        else:
            #display data value as bar graph
            value = float(hour["@Value"])
            values.append(value)
            if round(value) == 0:
                print(f"{hourTime} | ❚" + f" {value}")
            else:
                print(f"{hourTime} | " + "❚" * round(value) + f" {value}")

    print(f"--- Average Value ({site}, {species}) ---")

    from utils import meannvalue

    if len(values) != 0:
        #calculate average, rounding to 2 decimal places
        mean = round(meannvalue(values), 2)
        print(f"Average value for {species} at {site} = {mean}")
    else:
        print("No data available for average to be calculated.")