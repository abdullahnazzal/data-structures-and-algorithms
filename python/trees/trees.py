
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=None
        self.right=None

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




class Binary_Tree:
    """

    """
    def __init__(self):
        self.root=None

    def pre_order(self):
        output = []
        def walk(node):
            output.append(node.value)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        walk(self.root)
        return output

    def in_order(self):
        output = []
        def walk(node):
            if node.left:
                walk(node.left)
            output.append(node.value)
            if node.right:
                walk(node.right)
        walk(self.root)
        return output

    def post_order(self):
        output = []
        def walk(node):
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
            output.append(node.value)
        walk(self.root)
        return output

class Binary_Search_Tree(Binary_Tree):
    """
    This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods : Add , Contains
    """
    def add(self,value):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        """
        if not self.root:
            self.root=Node(value)
        else:
            self._add(value,self.root)
    def _add(self,value,cur_node):
        if value< cur_node.value:
            if not cur_node.left:
                cur_node.left=Node(value)
            else:
                self._add(value,cur_node.left)
        elif value> cur_node.value:
            if not cur_node.right:
                cur_node.right=Node(value)
            else:
                self._add(value,cur_node.right)
        else:
            print("Value is alredy in tree")
    def contains(self,value):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        if self.root:
            is_found=self._contains(value,self.root)
            if is_found:
                return True
            return False
        else:
            return None
    def _contains(self,value,cur_node):
        if value > cur_node.value and cur_node.right:
            return self._contains(value,cur_node.right)
        elif value < cur_node.value and cur_node.left:
            return self._contains(value,cur_node.left)
        if value == cur_node.value:
            return True
# bt=Binary_Tree()
# bst=Binary_Search_Tree()
# bst.add(1)
# bst.add(2)
# bst.add(3)
# bst.add(4)
# print(bst.contains(6))
