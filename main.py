# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification



def main_menu():
    """Displays text-based options to the user, providing information on different actions available.
    
    Inputs:
        [R, I, M, A, Q]: Strings representing the different actions available
        Other: Invalid input, user is informed to try again."""
    #prints text-based interface
    while True:
        print("--- Main Menu ---")
        print("R - Access the PR module")
        print("I - Access the MI module")
        print("M - Access the RM module")
        print("A - Print the About text")
        print("Q - Quit the Application")
        print("-----------------")
        choice = input("Select one of the options above: ")
        #checks input against different cases, executing the respective case block
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


def reporting_menu():
    """Runs functions responsible for the Pollution Reporting module."""
    print("--- Pollution Reporting ---")
    print("| MONITORING SITES |")
    print("M - Marylebone Road")
    print("N - N. Kensington")
    print("H - Harlington")
    print("---------------------------")
    print("? - Main Menu")
    valid1 = False
    while valid1 == False:
        siteChoice = input("Select a monitoring site, or return to main menu: ")
        #checks input against different cases, executing the respective case block
        match siteChoice:
            case "M":
                print("[Marlybone Road SELECTED]")
                site = "Marlybone Road"
                valid1 = True
            case "N":
                print("[N. Kensington SELECTED]")
                site = "N. Kensington"
                valid1 = True
            case "H":
                print("[Harlington SELECTED]")
                site = "Harlington"
                valid1 = True
            case "?":
                return
            case _:
                print("Invalid input given. Try again.")
                valid1 = False

    print("--- Pollution Reporting ---")
    print("| Pollutant |")
    print("NO - Nitric Oxide")
    print("PM10 - PM10 Inhalable Particulate Matter")
    print("PM25 - PM2.5 Inhalable Particulate Matter")
    print("---------------------------")
    print("? - Main Menu")
    valid2 = False
    while valid2 == False:
        pollChoice = input("Select a pollutant, or return to main menu: ")
        #checks input against different cases, executing the respective case block
        match pollChoice:
            case "NO":
                print("[Nitric Oxide SELECTED]")
                pollutant = "no"
                valid2 = True
            case "PM10":
                print("[PM10 SELECTED]")
                pollutant = "pm10"
                valid2 = True
            case "PM25":
                print("[PM2.5 SELECTED]")
                pollutant = "pm25"
                valid2 = True
            case "?":
                return
            case _:
                print("Invalid input given. Try again.")
                valid2 = False
        
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

    valid3 = False
    while valid3 == False:
        funcChoice = input("Select a function, or return to main menu: ")
        #checks input against different cases, executing the respective case block
        match funcChoice:
            case "1":
                valid3 = True
                from reporting import daily_average
                daily_average() # TODO: parse in correct data, including site and pollutant above
            case "2":
                valid3 = True
                from reporting import daily_median
                daily_median() # TODO: parse in correct data, including site and pollutant above
            case "3":
                valid3 = True
                from reporting import hourly_average
                hourly_average() # TODO: parse in correct data, including site and pollutant above
            case "4":
                valid3 = True
                from reporting import monthly_average
                monthly_average() # TODO: parse in correct data, including site and pollutant above
            case "5":
                valid3 = True
                from reporting import peak_hour_date
                peak_hour_date() # TODO: parse in correct data, including site and pollutant above
            case "6":
                valid3 = True
                from reporting import count_missing_data
                count_missing_data() # TODO: parse in correct data, including site and pollutant above
            case "7":
                valid3 = True
                from reporting import fill_missing_data
                fill_missing_data() # TODO: parse in correct data, including site and pollutant above
            case "?":
                return
            case _:
                valid3 = False
                print("Invalid input given. Try again.")


def intelligence_menu():
    """Displays text-based options to the user, providing information on different actions available.

    Inputs:
        [R, C, 1, 2]: Strings representing the different functions that can be selected
        ?: Returns user to main menu
        Other: Invalid input, user is informed to try again."""
    #prints text-based interface
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
    #checks input against different cases, executing the respective case block
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
    #prints text-based interface
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