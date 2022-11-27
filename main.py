# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification



def main_menu():
    """Displays text-based options to the user, providing information on different actions available.
    
    User Inputs:
        (String) [R, I, M]: Selects one of three different modules.
        (String) A: Prints the about section of the project.
        (String) Q: Quits the program.
        Other: Invalid input, user is informed to try again."""

    #prints text-based interface on a loop until the menu is exited
    while True:
        print("--- Main Menu ---")
        print("R - Access the PR module")
        print("I - Access the MI module")
        print("M - Access the RM module")
        print("A - Print the About text")
        print("Q - Quit the Application")
        print("-----------------")
        choice = input("Select one of the options above: ")
        #checks user input against different cases, executing the respective case block
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
    """Displays text-based options to the user, providing information on different actions available.

    User Inputs:
        (String) [M, N, H]: Selects one of three different monitoring sites.
        (String) [NO, PM10, PM25]: Selects one of three diffenent pollutants.
        (String) [1, 2, 3, 4, 5, 6, 7]: Selects one of seven different functions to perform.
        (String) ?: Returns user to main menu.
        Other: Invalid input, user is informed to try again.
        
    Returns:
        (None): Exits the current function to return to main menu."""

    validSite = False
    #loops until a valid input is given
    while validSite == False:
        #prints text-based interface
        print("--- Pollution Reporting ---")
        print("| MONITORING SITES |")
        print("M - Marylebone Road")
        print("N - N. Kensington")
        print("H - Harlington")
        print("---------------------------")
        print("? - Main Menu")

        siteChoice = input("Select a monitoring site, or return to main menu: ")
        #checks user input against different cases, executing the respective case block
        match siteChoice:
            case "M":
                print("[Marlybone Road SELECTED]")
                site = "Marlybone Road"
                validSite = True
            case "N":
                print("[N. Kensington SELECTED]")
                site = "N. Kensington"
                validSite = True
            case "H":
                print("[Harlington SELECTED]")
                site = "Harlington"
                validSite = True
            case "?":
                return
            case _:
                print("Invalid input given. Try again.")
                validSite = False

    validPoll = False
    #loops until a valid input is given
    while validPoll == False:
        #prints text-based interface
        print("--- Pollution Reporting ---")
        print("| Pollutant |")
        print("NO - Nitric Oxide")
        print("PM10 - PM10 Inhalable Particulate Matter")
        print("PM25 - PM2.5 Inhalable Particulate Matter")
        print("---------------------------")
        print("? - Main Menu")

        pollChoice = input("Select a pollutant, or return to main menu: ")
        #checks user input against different cases, executing the respective case block
        match pollChoice:
            case "NO":
                print("[Nitric Oxide SELECTED]")
                pollutant = "no"
                validPoll = True
            case "PM10":
                print("[PM10 SELECTED]")
                pollutant = "pm10"
                validPoll = True
            case "PM25":
                print("[PM2.5 SELECTED]")
                pollutant = "pm25"
                validPoll = True
            case "?":
                return
            case _:
                print("Invalid input given. Try again.")
                validPoll = False
        
    validFunc = False
    #loops until a valid input is given
    while validFunc == False:
        #prints text-based interface
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
        #checks user input against different cases, executing the respective case block
        match funcChoice:
            case "1":
                validFunc = True
                from reporting import daily_average
                daily_average() # TODO: parse in correct data, including site and pollutant above
            case "2":
                validFunc = True
                from reporting import daily_median
                daily_median() # TODO: parse in correct data, including site and pollutant above
            case "3":
                validFunc = True
                from reporting import hourly_average
                hourly_average() # TODO: parse in correct data, including site and pollutant above
            case "4":
                validFunc = True
                from reporting import monthly_average
                monthly_average() # TODO: parse in correct data, including site and pollutant above
            case "5":
                validFunc = True
                from reporting import peak_hour_date
                peak_hour_date() # TODO: parse in correct data, including site and pollutant above
            case "6":
                validFunc = True
                from reporting import count_missing_data
                count_missing_data() # TODO: parse in correct data, including site and pollutant above
            case "7":
                validFunc = True
                from reporting import fill_missing_data
                fill_missing_data() # TODO: parse in correct data, including site and pollutant above
            case "?":
                return
            case _:
                validFunc = False
                print("Invalid input given. Try again.")


def intelligence_menu():
    """Displays text-based options to the user, providing information on different actions available.

    User Inputs:
        (String) [R, C, 1, 2]: Selects one of four different functions to perform.
        (String) ?: Returns user to main menu.
        Other: Invalid input, user is informed to try again.
        
    Returns:
        (None): Exits the current function to return to main menu."""

    intelValid = False
    #loops until a valid input is given
    while intelValid == False:
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
        #checks user input against different cases, executing the respective case block
        match choice:
            case "R":
                intelValid = True
                from intelligence import find_red_pixels
                find_red_pixels()
            case "C":
                intelValid = True
                from intelligence import find_cyan_pixels
                find_cyan_pixels()
            case "1":
                intelValid = True
                from intelligence import detect_connected_components
                detect_connected_components()
            case "2":
                intelValid = True
                from intelligence import detect_connected_components_sorted
                detect_connected_components_sorted()
            case "?":
                return
            case _:
                intelValid = False
                print("Invalid input given. Try again.")


def monitoring_menu():
    # TODO: documentation
    pass


def about():
    """Displays text informing the user about the project.
    
    User Inputs:
        (Key Press) [enter key]: Returns the user back to the Main Menu.
        
    Returns:
        (None): Exits the current function to return to main menu."""

    #prints text-based interface
    print("--- About ---")
    print("Module Code: ECM1400")
    print("Candidate Number: 231682")
    print("-------------")
    input("Press Enter to return to Main Menu.")
    return


def quit():  
    """Exits the currently running program."""
    exit()



if __name__ == '__main__':
    main_menu()