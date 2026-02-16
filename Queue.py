Queue 
Example
from collections import deque

# Queue container
service_line = deque()

print("=== FIFO Queue Control System ===")

is_running = True
while is_running:
    print("\nQueue status:", list(service_line))
    print("Menu:")
    print("A. Add to queue")
    print("B. Remove from queue")
    print("C. View front item")
    print("D. Quit")

    user_input = input("Select option: ").lower().strip()

    if user_input == "a":
        value = input("Enter item to enqueue: ").strip()
        if value != "":
            service_line.append(value)
            print(f"'{value}' has been added to the queue.")
        else:
            print("Cannot add empty value.")

    elif user_input == "b":
        if service_line:
            served = service_line.popleft()
            print(f"'{served}' has been removed from the queue.")
        else:
            print("Queue is empty. Nothing to remove.")

    elif user_input == "c":
        if service_line:
            print("Front of queue:", service_line[0])
        else:
            print("Queue is currently empty.")

    elif user_input == "d":
        print("Queue system closed. Goodbye 👋")
        is_running = False

    else:
        print("Invalid input. Please choose A, B, C, or D.")
