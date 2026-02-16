Linked-list 
example
# Starting point of the linked list
start_node = None

print("=== Linked List Console Tool ===")

active = True
while active:
    print("\nMenu:")
    print("A. Add Node")
    print("B. Show List")
    print("C. Delete First Node")
    print("D. Exit")

    selection = input("Select an option: ").lower().strip()

    if selection == "a":
        value = input("Enter value for new node: ").strip()

        node = {
            "value": value,
            "link": None
        }

        # If list is empty, assign the new node as the starting node
        if start_node is None:
            start_node = node
        else:
            temp = start_node
            while temp["link"] is not None:
                temp = temp["link"]
            temp["link"] = node

        print(f"Node '{value}' successfully added.")

    elif selection == "b":
        if start_node is None:
            print("No nodes to display.")
        else:
            pointer = start_node
            print("\nSTART", end=" ")
            while pointer:
                print(f"--> ({pointer['value']})", end=" ")
                pointer = pointer["link"]
            print("--> NULL")

    elif selection == "c":
        if start_node:
            deleted_value = start_node["value"]
            start_node = start_node["link"]
            print(f"First node '{deleted_value}' has been deleted.")
        else:
            print("The list is already empty.")

    elif selection == "d":
        print("Exiting Linked List Tool. Goodbye!")
        active = False

    else:
        print("Invalid choice. Please select A, B, C, or D.")
