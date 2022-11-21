# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def main_menu():
    """Displays text-based options to the user, providing information on different actions available."""
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
            print("Invalid input given. Select an option listed above.")

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
    """Your documentation goes here"""
    # Your code goes here

def quit():
    """Your documentation goes here"""
    return




if __name__ == '__main__':
    main_menu()