# Singly Linked List
A Linked List is a sequence of **Nodes** that are connected/linked to each other. The most defining feature of a Linked List is that each **Node** references the next Node in the link.


## Challenge
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Create a Linked List class, include a head property ,insert, includes, to string methods.


## Approach & Efficiency
Singly

## API
**insert():**

Adds a new node with that value to the head of the list with an O(1) Time performance.

**includes():** 

Indicates whether that value exists as a Node’s value somewhere within the list.

**__str__():**

Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

**append()**

Adds a new node with the given value to the end of the list.

**insert_before()**

Adds a new node with the given new value immediately before the first node that has the value specified.

**insert_after()**

Adds a new node with the given new value immediately after the first node that has the value specified


