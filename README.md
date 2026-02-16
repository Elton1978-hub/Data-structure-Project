where the data structures types are applied ,reasons, examples of applications that are using the data structure type , algorithm , why  Research how data structures and algorithms work within systems.

Data-Structures-Assignment
Linear data structures are data structures whose elements are stored in non-hierarchical way where each element has the successors and predecessors except the first and last element. There are four types namely: Arrays, Stacks, Linked Lists, and Queues as illustrated below.
1. Arrays
Definition: A linear data structure that stores a collection of elements in contiguous memory locations. This allows the computer to calculate the position of any element using a mathematical formula based on its index.
Key Characteristics:
•	Fixed Size: Traditionally allocated with a set size; resizing requires creating a new array and copying data.
•	Zero-Based Indexing: The first element is at index 0.
•	Access Speed (O(1)): Direct access to any element via its index is nearly instantaneous.
•	Modification Speed (O(n)): Inserting or deleting from the middle requires "shifting" all subsequent elements to maintain the contiguous order.
•	Cache Friendliness: Due to contiguous storage, arrays are highly optimized for modern CPU architectures.
Best Use Case: When you need fast random access to data and the total number of elements stays relatively constant.
2. Stacks
Definition: A Stack is a linear data structure that serves as a collection of elements with two principal operations: push and pop. It operates on the Last-In, First-Out (LIFO) principle—meaning the most recent element added is the first one to be removed.
Real-World Analogy: Cafeteria Trays: You place a new tray on top of the pile (Push). When someone needs a tray, they take the one that was just placed there (Pop).
Key Characteristics:
•	Unidirectional: Access is restricted to a single end (The Top).
•	Recursive Nature: Stacks are used internally by operating systems to manage function calls (the "Call Stack").
•	Memory Efficiency: Since elements are only added/removed from the top, there is no need to "shift" elements like in an Array.
Operations:
•	Push: Adds an element to the Top of the stack.
•	Pop: Removes the element from the Top of the stack.
•	Peek: Returns the top element without removing it.
•	isEmpty: Checks if the stack contains any elements.
3. Queues
Definition: A Queue is a linear data structure that operates on the First-In, First-Out (FIFO) principle. In a queue, the first element added is the first one to be removed, much like a real-life waiting line.
Key Characteristics:
•	Enqueue: Adding an element to the back (rear) of the queue.
•	Dequeue: Removing an element from the front of the queue.
•	Peek/Front: Returns the front element without removing it.
•	IsFull/isEmpty: Checks the capacity or state of the queue
Real-world Analogy: The first person to arrive at the counter in a coffee shop is the first person served.
4. Linked Lists
Definition:
A Linked List is a linear data structure where elements are not stored in contiguous (adjacent) memory locations. Instead, the elements are linked using pointers.
Each element is called a Node, which acts as a container for both the data and the address of the next item in the sequence.
Real-world Analogy: A Scavenger Hunt. You find the first clue (Head), which tells you where the second clue is, which tells you where the third clue is.
The Head: The very first node in the list. If you lose the Head, you lose the whole list.
A node is typically represented as a record or object with two fields:
•	Data: The actual value being stored (Integer, String, etc.
•	Next: A reference (pointer) to the subsequent node. The last node's next pointer is null or None.
Key Characteristics:
•	Dynamic Size: Unlike standard arrays, linked lists can grow or shrink during execution without expensive resizing/copying.
•	Efficient Insertions/Deletions: Adding or removing elements doesn't require "shifting" the entire structure; you only need to update the pointers of the surrounding nodes.
•	Memory Overhead: Uses more memory than an array because it must store a next pointer for every single piece of data.
Operations:
•	Access/Search: Finding a specific value by traversing from the Head.
•	Insert (at Head): Creating a new node and making it the new Head.
•	Insert (at Tail): Traversing to the end to link a new node.
•	Delete (at Head) Moving the Head pointer to the second node

# Data-structure-Project
