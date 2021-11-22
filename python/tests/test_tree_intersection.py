from trees.trees import Node,Binary_Tree

from tree_intersection.tree_intersection import tree_intersection
import pytest

@pytest.fixture
def tree1():
    tree1 = Binary_Tree()
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    tree1.root=a_node
    tree1.in_order()
    return tree1
@pytest.fixture
def tree2():
    tree2 = Binary_Tree()
    a_node = Node(5)
    b_node = Node(3)
    c_node = Node(9)
    d_node = Node(2)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    tree2.root=a_node
    tree2.in_order()
    return tree2


def test_tree_intersection(tree1,tree2):
    """
    Successfully returns the common values in 2 binary trees.
    """
    expected = [3,2]
    actual = tree_intersection(tree1,tree2)
    assert actual == expected
