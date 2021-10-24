# Stacks and Queues
A **stack** is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

**Queue** is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first.



## Challenge
implement both a Stack and a Queue



## Approach & Efficiency


## API
Stack:
-   **push:**
adds a new node with that value to the top of the stack with an O(1) Time performance.
-   **pop:**
Removes the node from the top of the stack,
Should raise exception when called on empty stack,
and returns the value from node from the top of the stack.
-   **peek:**
Returns: Value of the node located at the top of the stack.
Should raise exception when called on empty stack.
-   **is_empty:**
Returns: Boolean indicating whether or not the stack is empty.

Queue:
-   **enqueue:**
adds a new node with that value to the back of the queue with an O(1) Time performance.
-   **dequeue:** 
Returns: the value from node from the front of the queue.
Removes the node from the front of the queue.
Should raise exception when called on empty queue.
-   **peek:**
Returns: Value of the node located at the front of the queue.
Should raise exception when called on empty stack.
-   **is_Empty:**
Returns: Boolean indicating whether or not the queue is empty.
