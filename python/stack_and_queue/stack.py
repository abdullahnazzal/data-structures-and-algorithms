from stack_and_queue.node import Node
class Stack:

    def __init__(self):
        self.top=None

    def push(self,value):
        """
        adds a new node with that value to the top of the stack with an O(1) Time performance.
        """
        node=Node(value)
        node.next_node=self.top
        self.top=node

    def pop(self):
        """
        Removes the node from the top of the stack,
        Should raise exception when called on empty stack,
        and returns the value from node from the top of the stack.
        """
        if self.top:
            temp=self.top
            self.top=self.top.next_node
            temp.next_node=None
            return temp.value
        else:
            raise Exception("The stack is empte")

    def peek(self):
        """
        Returns: Value of the node located at the top of the stack.
        Should raise exception when called on empty stack.
        """
        if self.top:
            return self.top.value
        else:
            raise Exception("The stack is empte")

    def is_empty(self):
        """
        Returns: Boolean indicating whether or not the stack is empty.
        """
        if self.top==None:
            return True
        return False
        
