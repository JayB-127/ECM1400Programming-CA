# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def main_menu():
    """Displays text-based options to the user, providing information on different actions available.
    
    Inputs:
        R, I, M, A, Q: The function for the corresponding action is performed
        Other: A statement is printed to the user, requesting a valid input"""
    print("R - Access the PR module")
    print("I - Access the MI module")
    print("M - Access the RM module")
    print("A - Print the About text")
    print("Q - Quit the Application")
    choice = input("Select one of the options above: ")
    match choice:
        case "R":
            #PR module
            reporting_menu()
        case "I":
            #MI module
            monitoring_menu()
        case "M":
            #RM module
            intelligence_menu()
        case "A":
            #About text
            about()
        case "Q":
            #Quit application
            quit()
        case _:
            print("Invalid input given. Try again.")
            main_menu()

def reporting_menu():
    """Your documentation goes here"""
    # Your code goes here

def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here

def intelligence_menu():
    """Your documentation goes here"""
    # Your code goes here

def about():
    """Displays text informing the user about the project.
    
    Inputs:
        [enter key]: Returns the user back to the Main Menu"""
    print("-- ABOUT --")
    print("Module Code: ECM1400")
    print("Candidate Number: 231682")
    print("-----------")
    input("Press Enter to return to Main Menu.")
    main_menu()

def quit():
    """Exits the currently running program."""
    exit()




if __name__ == '__main__':
    main_menu()