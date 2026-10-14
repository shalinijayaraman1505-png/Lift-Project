current_floor = 0

print("Current floor:", current_floor)


def select_floor():
    destination_floor = int(input("Which floor do you want to go to (0-4)? "))
    return destination_floor


def move_lift():
    global current_floor

    destination_floor = select_floor()

    if destination_floor < 0 or destination_floor > 4:
        print("Invalid floor! Please select a floor between 0 and 4.")

    elif destination_floor > current_floor:
        print("Lift is moving up")
        current_floor = destination_floor

    elif destination_floor < current_floor:
        print("Lift is moving down")
        current_floor = destination_floor

    else:
        print("Lift is already at this floor")

    print("Current floor:", current_floor)


def show_menu():
    print("\n===== LIFT MENU =====")
    print("1. Select Floor")
    print("2. Exit")
    print("3. Check Current Floor")
    print("4. Show All Available Floors")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        move_lift()

    elif choice == "2":
        print("Lift is stopped.")
        break

    elif choice == "3":
        print("Current floor:", current_floor)

    elif choice == "4":
        print("Available floors: 0, 1, 2, 3, 4")

    else:
        print("Invalid choice!")
