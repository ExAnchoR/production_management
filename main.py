
from view.menu import Menu

if __name__ == "__main__":
    menu_instance = Menu()

    # Loop to handle the sequence of login and main menu
    while True:
        # Ask staff to register, login, or exit
        authenticated = menu_instance.show_Staff_Auth()

        # If login is successful, open the main production dashboard
        if authenticated:
            menu_instance.show_menu()
        else:
            # Exit the program if the user chooses Exit
            break
