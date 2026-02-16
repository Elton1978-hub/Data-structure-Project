Stack
Example:
my_stack = []

print("--- Simple Stack Manager (LIFO) ---")

while True:
    # Display the current stack (top is the last item in the list)
    print("\n--- Current Stack (Last at the top) ---")
    for item in reversed(my_stack):
        print(f"| {item} |")
    print("-------")
    print("Options: 1. Push (Add) | 2. Pop (Remove) | 3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter value to PUSH onto the stack: ")
        my_stack.append(item) # Adds to the end (the top)
        print(f"Added {item} to the top.")

    elif choice == "2":
        if len(my_stack) > 0:
            # .pop() automatically removes the LAST item added
            removed_item = my_stack.pop() 
            print(f"POPPED '{removed_item}' from the top.")
        else:
            print("The stack is empty! Nothing to pop.")

    elif choice == "3":
        print("Exiting stack demo...")
        break
    else:

        print("Invalid choice.")

