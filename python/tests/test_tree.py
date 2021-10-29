from trees.trees import Node,Binary_Tree,Binary_Search_Tree
def test_empty_tree():
    """
    Can successfully instantiate an empty tree
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    assert tree.root == None

def test_tree_with_one_node():
    """
    Can successfully instantiate a tree with a single root node
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Add Root node to tree
    tree.root=1
    # set expected list
    expected = 1
    # set actual to return value of one node
    actual = tree.root
    # assert actual is same as expected
    assert actual == expected

def test_tree_with_left_and_right_child():
    """
    Can successfully add a left child and right child to a single root node
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    a_node.left = b_node
    a_node.right = c_node
    # Add Root node to tree
    tree.root=a_node
    # set expected list
    expected_left = tree.root.left.value
    expected_right = tree.root.right.value
    # set actual to return value of left child and right child to a single root node
    actual_left = 2
    actual_right = 3
    # assert actual is same as expected
    assert actual_left == expected_left
    assert actual_right == expected_right


def test_tree_pre_order():
    """
    Can successfully return a collection from a preorder traversal
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node
    # set expected list
    expected = [1,2,4,3]
    # set actual to return value of pre_order call
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected

def test_tree_in_order():
    """
    Can successfully return a collection from an inorder traversal.
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node
    # set expected list
    expected = [4,2,1,3]
    # set actual to return value of in_order call
    actual = tree.in_order()
    # assert actual is same as expected
    assert actual == expected

def test_tree_post_order():
    """
    Can successfully return a collection from a postorder traversal.
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node
    # set expected list
    expected = [4,2,3,1]
    # set actual to return value of post_order call
    actual = tree.post_order()
    # assert actual is same as expected
    assert actual == expected





















# def test_bfs():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for A,B,C,D
#   a_node = Node('A')
#   b_node = Node('B')
#   c_node = Node('C')
#   d_node = Node('D')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node 
  
#   # set expected list
#   expected = ["A", "B", "C", "D"]
#   # set actual to return value of bfs call
#   actual = tree.bfs()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_bfs passed")

# def test_bfs_2():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for A,B,C,D
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node 
  
#   # set expected list
#   expected = ["1", "2", "3", "4"]
#   # set actual to return value of bfs call
#   actual = tree.bfs()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_bfs_2 passed")



# def test_pre_order():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for 1,2,3,4
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node 
  
#   # set expected list
#   expected = ["1", "2", "4", "3"]
#   # set actual to return value of pre_order call
#   actual = tree.pre_order()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_pre_order_ passed")

# def test_post_order():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for 1,2,3,4
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node 
  
#   # set expected list
#   expected = ["4", "2", "3", "1"]
#   # set actual to return value of post_order call
#   actual = tree.post_order()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_post_order_ passed")  

# def test_in_order():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for 1,2,3,4
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node 
  
#   # set expected list
#   expected = ["4", "2", "1", "3"]
#   # set actual to return value of in_order call
#   actual = tree.in_order()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_in_order_ passed")