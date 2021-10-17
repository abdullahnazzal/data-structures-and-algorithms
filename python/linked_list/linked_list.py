from typing import Any


class Node:
    """
    class Node to represent the node

    properties:
    data = value stored in the Node
    next_node = a pointer to the next Node
    """
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node

class LinkedList:
    """
    A class for creating instances of a Linked List.
  
    Attributes defined here:
    
    head: Node | None
    current: head | head

    Methods defined here

    insert(value: any)
    contains(value: any) -> bool

    """
    def __init__(self):
        # initialization here
        self.head=None
        self.current=self.head

    def insert(self,value):
        """
        Adds a new node with that value to the head of the list with an O(1) Time performance.

        Arguments: value
        Returns: nothing
        """
        self.head=Node(value,self.head)
        self.current=self.head
    

    def includes(self,value=None):
        """
        Indicates whether that value exists as a Node’s value somewhere within the list.

        Arguments: value
        Returns: Boolean
        """
        while self.current != None:
            if self.current.value==value:
                return True
            self.current=self.current.next_node
        return False
    
    def __str__(self):
        """
        To convert Linked List as string formatted
        Arguments: none
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        string_list=""
        self.current=self.head
        while self.current != None:
            string_list+="{ "+"{}".format(self.current.value)+" } -> "
            self.current=self.current.next_node
            if self.current == None:
                string_list+="NULL"
        
        return string_list

# linked_list=LinkedList()
# linked_list.insert(6)
# linked_list.includes(5)
# print(linked_list.includes(6))
# print(linked_list.head.data)
# linked_list.insert(7)
# linked_list.insert(9)
# print(linked_list.head.data)
# linked_list.includes()
# print(linked_list.includes(6))
# linked_list.print_listedlink()
# linked_list.to_string()

# print(linked_list.to_string())