# Kyle Draghi
# Midterm Project

# Create an empty dictionary
inventory = {}

# Main Menu
def mainMenu():
    print("############# Main Menu #############")
    print("1: Add items(s) to your inventory")
    print("2: Remove item(s) in your inventory")
    print("3: Update amount of item(s) in your inventory")
    print("4: View your inventory")
    print("5: Clear your inventory and start over")
    print("6: Exit")

# Prompt user to enter how many item(s) they want to add to the inventory
def add_to_inventory():
    # Use Try/Except for user value error
    while True:
        try:
            n = int(input("How many items would you like to add to your inventory?: "))
        except ValueError:
            print("Invalid input. Not an integer. Please try again.")
            continue
        else:
            break

    # Loop through amount user enters and add item(s) and their amount
    for item in range(0, n):
        item = input("Enter item you want to add to your inventory: ").lower().strip()
        while True:
            try:
                amount = int(input("Enter the amount of item: "))
            except ValueError:
                print("Invalid input. Not an integer. Please try again.")
                continue
            else:
                break
        inventory[item] = amount
        print("Item successfully added!")
    main()
