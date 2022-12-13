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
        #checks user input against different conditions, executing the respective block
        if choice.upper() == "R":
            reporting_menu()
        elif choice.upper() == "I":
            intelligence_menu()
        elif choice.upper() == "M":
            monitoring_menu()
        elif choice.upper() == "A":
            about()
        elif choice.upper() == "Q":
            quit()
        else:
            print("Invalid input given. Try again.")


def reporting_menu():
    """Displays text-based options to the user, providing information on different actions available.

    User Inputs:
        (String) [M, N, H]: Selects one of three different monitoring stations.
        (String) [NO, PM10, PM25]: Selects one of three diffenent pollutants.
        (String) [1, 2, 3, 4, 5, 6, 7]: Selects one of seven different functions to perform.
        (String) ?: Returns user to main menu.
        Other: Invalid input, user is informed to try again.
        
    Returns:
        (None): Exits the current function to return to main menu."""

    validStation = False
    #loops until a valid input is given
    while not validStation:
        #prints text-based interface
        print("--- Pollution Reporting ---")
        print("| MONITORING STATIONS |")
        print("M - Marylebone Road")
        print("N - N. Kensington")
        print("H - Harlington")
        print("---------------------------")
        print("? - Main Menu")

        stationChoice = input("Select a monitoring station , or return to main menu: ")
        #checks user input against different conditions, executing the respective block
        if stationChoice.upper() == "M":
            validStation = True
            print("[Marylebone Road SELECTED]")
            station = "Marylebone Road"
        elif stationChoice.upper() == "N":
            validStation = True
            print("[N. Kensington SELECTED]")
            station = "N Kensington"
        elif stationChoice.upper() == "H":
            validStation = True
            print("[Harlington SELECTED]")
            station = "Harlington"
        elif stationChoice == "?":
            return
        else:
            validStation = False
            print("Invalid input given. Try again.")

    validPoll = False
    #loops until a valid input is given
    while not validPoll:
        #prints text-based interface
        print("--- Pollution Reporting ---")
        print("| Pollutant |")
        print("NO - Nitric Oxide")
        print("PM10 - PM10 Inhalable Particulate Matter")
        print("PM25 - PM2.5 Inhalable Particulate Matter")
        print("---------------------------")
        print("? - Main Menu")

        pollChoice = input("Select a pollutant, or return to main menu: ")
        #checks user input against different conditions, executing the respective block
        if pollChoice.upper() == "NO":
            validPoll = True
            print("[Nitric Oxide SELECTED]")
            pollutant = "no"
        elif pollChoice.upper() == "PM10":
            validPoll = True
            print("[PM10 SELECTED]")
            pollutant = "pm10"
        elif pollChoice.upper() == "PM25":
            validPoll = True
            print("[PM2.5 SELECTED]")
            pollutant = "pm25"
        elif pollChoice == "?":
            return
        else:
            validPoll = False
            print("Invalid input given. Try again.")
        
    validFunc = False
    #loops until a valid input is given
    while not validFunc:
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
        #checks user input against different conditions, executing the respective block
        if funcChoice == "1":
            validFunc = True
            from reporting import daily_average, get_data
            list = daily_average(get_data(), station , pollutant)
            i = 1
            for x in list:
                print(f"Day {i}: {x}")
                i += 1
        elif funcChoice == "2":
            validFunc = True
            from reporting import daily_median, get_data
            list = daily_median(get_data(), station , pollutant)
            i = 1
            for x in list:
                print(f"Day {i}: {x}")
                i += 1
        elif funcChoice == "3":
            validFunc = True
            from reporting import hourly_average, get_data
            list = hourly_average(get_data(), station , pollutant)
            i = 1
            for x in list:
                time = "%02d:00:00" %i
                print(f"{time}: {x}")
                i += 1
        elif funcChoice == "4":
            validFunc = True
            from reporting import monthly_average, get_data
            list = monthly_average(get_data(), station , pollutant)
            i = 1
            for x in list:
                print(f"Month {i}: {x}")
                i += 1
        elif funcChoice == "5":
            validFunc = True
            from reporting import peak_hour_date, get_data
            date = input("Enter a date in YYYY-MM-DD format: ")
            hour, value = peak_hour_date(get_data(), date, station , pollutant)
            print(f"Peak hour for {date}: {hour} with a value of {value}")
        elif funcChoice == "6":
            validFunc = True
            from reporting import count_missing_data, get_data
            count = count_missing_data(get_data(), station , pollutant)
            print(f"There are {count} occurences of 'No data' for {pollutant} in {station}")
        elif funcChoice == "7":
            validFunc = True
            from reporting import fill_missing_data, get_data
            new_value = input("Enter a value to replace 'No data': ")
            fill_missing_data(get_data(), new_value, station , pollutant)
        elif funcChoice == "?":
            return
        else:
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
    while not intelValid:
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

        from intelligence import find_red_pixels, find_cyan_pixels

        funcChoice = input("Select a function, or return to main menu: ")
        #checks user input against different conditions, executing the respective block
        if funcChoice.upper() == "R":
            intelValid = True
            #get user input for filename, catching an exception if the file is not found
            try:
                map_filename = "data/" + input("Enter a filename for an existing city map image (exclude file extension): ") + ".png"
                find_red_pixels(map_filename, 100, 50)
            except FileNotFoundError:
                print("File Not Found. Try again.")
        elif funcChoice.upper() == "C":
            intelValid = True
            #get user input for filename, catching an exception if the file is not found
            try:
                map_filename = "data/" + input("Enter a filename for an existing city map image (exclude file extension): ") + ".png"
                find_cyan_pixels(map_filename, 100, 50)
            except FileNotFoundError:
                print("File Not Found. Try again.")
        elif funcChoice == "1":
            intelValid = True
            from intelligence import detect_connected_components
            colourChoice = input("Red - [R] or Cyan - [C]: ")
            if colourChoice.upper() == "R":
                try:
                    map_filename = "data/" + input("Enter a filename for an existing city map image (exclude file extension): ") + ".png"
                    img = find_red_pixels(map_filename, 100, 50)
                    detect_connected_components(img)
                except FileNotFoundError:
                    print("File Not Found. Try again.")
            elif colourChoice.upper() == "C":
                try:
                    map_filename = "data/" + input("Enter a filename for an existing city map image (exclude file extension): ") + ".png"
                    img = find_cyan_pixels(map_filename, 100, 50)
                    detect_connected_components(img)
                except FileNotFoundError:
                    print("File Not Found. Try again.")
            else:
                print("Invalid input given. Try again.")
        elif funcChoice == "2":
            intelValid = True
            from intelligence import detect_connected_components, detect_connected_components_sorted
            colourChoice = input("Red - [R] or Cyan - [C]: ")
            if colourChoice.upper() == "R":
                try:
                    map_filename = "data/" + input("Enter a filename for an existing city map image (exclude file extension): ") + ".png"
                    img = find_red_pixels(map_filename, 100, 50)
                    mark = detect_connected_components(img)
                    detect_connected_components_sorted(mark)
                except FileNotFoundError:
                    print("File Not Found. Try again.")
            elif colourChoice.upper() == "C":
                try:
                    map_filename = "data/" + input("Enter a filename for an existing city map image (exclude file extension): ") + ".png"
                    img = find_cyan_pixels(map_filename, 100, 50)
                    mark = detect_connected_components(img)
                    detect_connected_components_sorted(mark)
                except FileNotFoundError:
                    print("File Not Found. Try again.")
            else:
                print("Invalid input given. Try again.")
        elif funcChoice == "?":
            return
        else:
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