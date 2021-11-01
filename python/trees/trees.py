
class Node:
    def __init__(self,value,next_node=None,left=None,right=None):
        self.value=value
        self.left=None
        self.right=None
        self.next_node=None
class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False
    
  def enqueue(self,item):
    self.data.append(item)
    
  def dequeue(self):
    return self.data.pop(0)
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
    def find_maximum_value(self):
        """
        
        Arguments: none
        Returns: number
        Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
        """
        max_value = self.root.value
        def walk(node):
            nonlocal max_value
            if node.left:
                if node.left.value > max_value:
                    max_value=node.left.value
                walk(node.left)
            if node.right:
                if node.right.value > max_value:
                    max_value=node.right.value
                walk(node.right)
        walk(self.root)
        return max_value
            
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
    


def breadth_first(tree):
    """
    Return list of all values in the tree using a Breadth-first approach.
    """
    output = []
    breadth = Queue()
    breadth.enqueue(tree.root)
    # print(tree.root.value)
    while breadth.peek():
        front = breadth.dequeue()
        print(front.value)
        output.append(front.value)
        # output.append(front.value)
        if front.left:
            print("left")
            breadth.enqueue(front.left)
        
        if front.right:
            breadth.enqueue(front.right)

    return output
bt=Binary_Tree()
bst=Binary_Search_Tree()
# bst.add(50)
# bst.add(2)
# bst.add(3)
# bst.add(1)
# bst.add(15)
# bst.add(10)
a_node = Node(1)
b_node = Node(2)
c_node = Node(50)
d_node = Node(20)
a_node.left = b_node
a_node.right = c_node
b_node.left = d_node

bt.root=a_node
# print(bst.find_maximum_value())
print(breadth_first(bt))
