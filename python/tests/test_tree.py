from trees.trees import Node,Binary_Tree,Binary_Search_Tree,breadth_first,NodeK
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

def test_find_maximum_value_in_tree():
    """
    Can successfully return maximum value stored in the tree.
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(50)
    d_node = Node(20)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node
    # set expected value
    expected = 50
    # set actual to return maximum value.
    actual = tree.find_maximum_value()
    # assert actual is same as expected
    assert actual == expected

def test_breadth_first():
    """
    Can successfully return list of all values in the tree using a Breadth-first approach.
    """
    # Arrange
    # Create tree instance
    tree = Binary_Tree()
    # Create Nodes for 1,2,50,20
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(50)
    d_node = Node(20)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node
    # set expected value
    expected = [1,2,50,20]
    # set actual to return list of all values.
    actual = breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected

def fizz_buzz_tree():
    """
    Can successfully return list of all values in the tree using a Breadth-first approach.
    """
    # Arrange
    root = NodeK(57)

    node1 = NodeK(15)
    root.children.append(node1)
    node1.children.append(NodeK(12))
    node1.children.append(NodeK(5))
    node1.children.append(NodeK(6))
    node1.parent=root

    node2 = NodeK(8)
    root.add_child(node2)
    node2.add_child(NodeK(9))
    node2.add_child(NodeK(4))
    node2.add_child(NodeK(5))

    node3 = NodeK(11)
    root.add_child(node3)
    node3.add_child(NodeK(687))
    node3.add_child(NodeK(98))
    # set expected value
    expected = ['Fizz', 12, 'Buzz', 'Fizz', 6, 'Fizz', 9, 4, 'Buzz', 'Fizz', 687, 98]
    # set actual to return list of all values.
    actual = root.fizz_buzz_tree()
    # assert actual is same as expected
    assert actual == expected
