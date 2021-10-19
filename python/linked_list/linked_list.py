from typing import Any, Counter


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
        self.lenght=0

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
        # newNode=Node(value)
        # if(self.head):
        #     self.current=self.head
        #     while(self.current.next_node):
        #         self.current=self.current.next_node
        #     self.current.next_node=newNode
        # else:
        #     self.head=newNode

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

    def append(self,value):
            """
            adds a new node with the given value to the end of the list.

            Arguments: new value
            Returns: nothing
            """
            newNode=Node(value)
            if(self.head):
                self.current=self.head
                while(self.current.next_node):
                    self.current=self.current.next_node
                self.current.next_node=newNode
            else:
                self.head=newNode
            # self.head=Node(value,self.head)
            # self.current=self.head
    def insert_before(self,next_node,value):
        """
        insert before
        arguments: value, new value
        Adds a new node with the given new value immediately before the first node that has the value specified
        """
        if self.head is None:
            return 
        if self.head.value== next_node:
            newNode=Node(value)
            newNode.next_node=self.head
            self.head=newNode
            return
        n=self.head
        while n.next_node is not None:
            if n.next_node.value==next_node:
                break
            n=n.next_node
        if n.next_node is None:
            print("Node is not found")
        else:
            newNode=Node(value)
            newNode.next_node=n.next_node
            n.next_node=newNode

    def insert_after(self,next_node,value):
        """
        insert after
        arguments: value, new value
        Adds a new node with the given new value immediately after the first node that has the value specified

        """
        n=self.head
        
        while n is not None:
            if n.value==next_node:
                break
            n=n.next_node
        if n is None:
            print("Node is not present in Linked List")
        else:
            newNode=Node(value)
            newNode.next_node=n.next_node
            n.next_node=newNode
    def kthFromEnd(self,k):
        """
        argument: a number, k, as a parameter.

        Return the node’s value that is k places from the tail of the linked list.
        You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

        """
        current=self.head
        lenght=0
        while current:
            current=current.next_node
            lenght+=1
        if lenght >= k:
            current=self.head
            for i in range (lenght -k-1):
                current=current.next_node
        else:
            return "K is bigger than nodes number"
        return current.value

linked_list=LinkedList()
linked_list.insert(2)
# linked_list.includes(5)
print(linked_list.includes(6))
# print(linked_list.head.data)
linked_list.insert(8)
linked_list.insert(3)
linked_list.insert(1)
# print(linked_list.head.data)
# linked_list.includes()
print(linked_list.includes(6))
# linked_list.print_listedlink()
# linked_list.to_string()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.add_before(50,6)

# linked_list.insert_before(9,50)
# linked_list.insert_after(9,100)
print(linked_list.__str__())
print(linked_list.kthFromEnd(0))