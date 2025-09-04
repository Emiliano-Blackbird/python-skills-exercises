print("Welcome to the Bank System")
while True:
    print("1 - Enter Bank account")
    print("2 - Withdraw money")
    print("3 - Pay bills")
    print("4 - Change password")
    print("5 - Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        print("You have chosen to enter your bank account.")
    elif option == 2:
        print("You have chosen to withdraw money.")
    elif option == 3:
        print("You have chosen to pay bills.")
    elif option == 4:
        print("You have chosen to change your password.")
    elif option == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
print("Program has ended.")
