1.Array
Example
# List to store user data
data_list = []

print("=== Interactive List Controller ===")

running = True
while running:
    print("\nCurrent items:", data_list)
    print("Choose an action:")
    print("A - Insert item")
    print("B - Delete item")
    print("C - Quit program")

    user_choice = input("Enter your choice: ").lower().strip()

    if user_choice == "a":
        value = input("Enter a value to insert: ").strip()

        if value != "":
            data_list.append(value)
            print(f"Success! '{value}' has been added.")
        else:
            print("Invalid input. Empty values are not allowed.")

    elif user_choice == "b":
        value = input("Enter a value to delete: ").strip()

        if value in data_list:
            data_list.remove(value)
            print(f"Done! '{value}' has been removed.")
        else:
            print("Item not found in the list.")

    elif user_choice == "c":
        print("Program terminated. See you next time 👋")
        running = False

    else:
        print("Invalid option. Please select A, B, or C.")
