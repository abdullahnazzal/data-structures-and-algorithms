class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=None

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
        temp=self.top
        self.top=self.top.next_node
        temp.next_node=None
        return temp.value

    def peek(self):
        """
        Returns: Value of the node located at the top of the stack.
        Should raise exception when called on empty stack.
        """
        if self.top:
            return self.top.value
        else:
            raise Exception("The stack is empty")

class PseudoQueue:
    """
        this PseudoQueue class will implement our standard queue interface (the two methods listed below),
        Internally, utilize 2 Stack instances to create and manage the queue
    """
    def __init__(self):
        self.first_stack=Stack()
        self.second_stack=Stack()
    
    def enqueue(self,value):
        """
        Arguments: value
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.first_stack.push(value)

    def dequeue(self):
        """
        Arguments: none
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.h

        """
        if self.second_stack.top == None:
            if self.first_stack.top == None:
                raise Exception("The queue is empty")
            while self.first_stack.top != None:
                item=self.first_stack.pop()
                self.second_stack.push(item)
        return self.second_stack.pop()
        

q = PseudoQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
# q.enqueue(4)
print(q.dequeue())
# print(q.dequeue())
