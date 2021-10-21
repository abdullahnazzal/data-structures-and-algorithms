from stack_and_queue.node import Node
class Queue:
    
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next_node=node
            self.rear=node
    
    def dequeue(self):
        """
        Returns: the value from node from the front of the queue.
        Removes the node from the front of the queue.
        Should raise exception when called on empty queue.
        """
        if self.front:
            temp=self.front
            self.front=self.front.next_node
            temp.next_node=None
            return temp.value
        else:
            raise Exception("The queue is empty")
    
    def peek(self):
        """
        Returns: Value of the node located at the front of the queue.
        Should raise exception when called on empty stack.
        """
        if self.front:
            return self.front.value
        else:
            raise Exception("The queue is empty")
    
    def is_Empty(self):
        """
        Returns: Boolean indicating whether or not the queue is empty
        """
        if self.front:
            return True
        else:
            return False



    