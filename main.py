# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification



def main_menu():
    """Displays text-based options to the user, providing information on different actions available.
    
    Inputs:
        [R, I, M, A, Q]: The function for the corresponding action is run
        Other: A statement is printed to the user, requesting a valid input"""
    print("--- Main Menu ---")
    print("R - Access the PR module")
    print("I - Access the MI module")
    print("M - Access the RM module")
    print("A - Print the About text")
    print("Q - Quit the Application")
    print("-----------------")
    choice = input("Select one of the options above: ")
    match choice:
        case "R":
            reporting_menu()
        case "I":
            intelligence_menu()
        case "M":
            monitoring_menu()
        case "A":
            about()
        case "Q":
            quit()
        case _:
            print("Invalid input given. Try again.")
            main_menu()
            exit()


def reporting_menu():
    # TODO: documentation
    site = siteChoice()
    pollutant = pollutantChoice()
    functionChoice(site, pollutant)

def siteChoice():
    # TODO: documentation
    print("--- Pollution Reporting ---")
    print("| MONITORING SITES |")
    print("M - Marylebone Road")
    print("N - N. Kensington")
    print("H - Harlington")
    print("---------------------------")
    print("? - Main Menu")
    siteChoice = input("Select a monitoring site, or return to main menu: ")
    match siteChoice:
        case "M":
            print("[Marlybone Road SELECTED]")
            return "Marlybone Road"
        case "N":
            print("[N. Kensington SELECTED]")
            return "N. Kensington"
        case "H":
            print("[Harlington SELECTED]")
            return "Harlington"
        case "?":
            main_menu()
        case _:
            print("Invalid input given. Try again.")
            reporting_menu()

def pollutantChoice():
    # TODO: documentation
    print("--- Pollution Reporting ---")
    print("| Pollutant |")
    print("NO - Nitric Oxide")
    print("PM10 - PM10 Inhalable Particulate Matter")
    print("PM25 - PM2.5 Inhalable Particulate Matter")
    print("---------------------------")
    print("? - Main Menu")
    pollChoice = input("Select a pollutant, or return to main menu: ")
    match pollChoice:
        case "NO":
            print("[Nitric Oxide SELECTED]")
            return "no"
        case "PM10":
            print("[PM10 SELECTED]")
            return "pm10"
        case "PM25":
            print("[PM2.5 SELECTED]")
            return "pm25"
        case "?":
            main_menu()
        case _:
            print("Invalid input given. Try again.")
            pollutantChoice()

def functionChoice(site, pollutant):
    # TODO: documentation
    site = site
    pollutant = pollutant
    print("--- Pollution Reporting ---")
    print("| Analysis Functions |")
    print("1 - Daily Average")
    print("2 - Daily Median")
    print("3 - Hourly Average")
    print("4 - Monthly Average")
    print("5 - Peak Hour Data")
    print("| Missing Data Functions |")
    print("6 - Count Missing Data")
    print("7 - Fill Missing Data")
    print("---------------------------")
    print("? - Main Menu")
    funcChoice = input("Select a function, or return to main menu: ")
    match funcChoice:
        case "1":
            from reporting import daily_average
            daily_average() # TODO: parse in correct data, including site and pollutant above
        case "2":
            from reporting import daily_median
            daily_median() # TODO: parse in correct data, including site and pollutant above
        case "3":
            from reporting import hourly_average
            hourly_average() # TODO: parse in correct data, including site and pollutant above
        case "4":
            from reporting import monthly_average
            monthly_average() # TODO: parse in correct data, including site and pollutant above
        case "5":
            from reporting import peak_hour_date
            peak_hour_date() # TODO: parse in correct data, including site and pollutant above
        case "6":
            from reporting import count_missing_data
            count_missing_data() # TODO: parse in correct data, including site and pollutant above
        case "7":
            from reporting import fill_missing_data
            fill_missing_data() # TODO: parse in correct data, including site and pollutant above
        case "?":
            main_menu()
        case _:
            print("Invalid input given. Try again.")
    functionChoice(site, pollutant)


def intelligence_menu():
    # TODO: documentation
    print("--- Mobility Intelligence ---")
    print("| Find Pixels |")
    print("R - Find Red Pixels")
    print("C - Find Cyan Pixels")
    print("| Connected Components |")
    print("1 - Detect Connected Components")
    print("2 - Sort Connected Components")
    print("-----------------------------")
    print("? - Main Menu")
    choice = input("Select a function, or return to main menu: ")
    match choice:
        case "R":
            from intelligence import find_red_pixels
            find_red_pixels()
        case "C":
            from intelligence import find_cyan_pixels
            find_cyan_pixels()
        case "1":
            from intelligence import detect_connected_components
            detect_connected_components()
        case "2":
            from intelligence import detect_connected_components_sorted
            detect_connected_components_sorted()
        case "?":
            main_menu()
        case _:
            print("Invalid input given. Try again.")
    intelligence_menu()


def monitoring_menu():
    # TODO: documentation
    pass


def about():
    """Displays text informing the user about the project.
    
    Inputs:
        [enter key]: Returns the user back to the Main Menu"""
    print("--- About ---")
    print("Module Code: ECM1400")
    print("Candidate Number: 231682")
    print("-------------")
    input("Press Enter to return to Main Menu.")
    main_menu()


def quit():  
    """Exits the currently running program."""
    exit()



if __name__ == '__main__':
    main_menu()