from typing import Any
from linked_list.linked_list import LinkedList,Node
import pytest

def test_import():
    assert LinkedList

def test_node_has_integer_value():
    #Arrange
    node=Node(1)
    expected = 1

    #Act
    actual =node.value
    #Assert
    assert actual== expected

def test_node_has_string_value():
    #Arrange
    node=Node("a")
    expected = "a"

    #Act
    actual =node.value
    #Assert
    assert actual== expected

def test_node_is_a_Node():
    #Arrange
    node=Node("")
    expected = "Node"

    #Act
    actual =type(node).__name__
    #Assert
    assert actual== expected

def test_node_witout_value():
    with pytest.raises(TypeError):
        node = Node()

def test_new_linked_List_is_empty():
    #Arrange
    linked_list=LinkedList()
    expected = None

    #Act
    actual =linked_list.head
    #Assert
    assert actual== expected

def test_linked_List_insert():
    #Arrange
    linked_list=LinkedList()
    linked_list.insert(6)
    expected = 6

    #Act
    actual =linked_list.head.value
    #Assert
    assert actual== expected

def test_linked_List_insert_twice():
    # Arrange
    expected = 0
    linked_list = LinkedList()

    # Act
    linked_list.insert(1)
    linked_list.insert(0)
    node = linked_list.head
    actual = node.value

    # Assert
    assert actual == expected
    assert linked_list.head.next_node.value == 1

def test_a_value_includes_in_linked_List():
    # Arrange
    linked_list = LinkedList()
    expected = True

    # Act
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.includes(2)

    # Assert
    assert actual == expected

def test_a_value_not_includes_in_linked_List():
    # Arrange
    linked_list = LinkedList()
    expected = False

    # Act
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.includes(5)

    # Assert
    assert actual == expected

def test_linked_List_to_string():
    # Arrange
    linked_list = LinkedList()
    expected = '{ 3 } -> { 2 } -> { 1 } -> NULL'
                

    # Act
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.__str__()

    # Assert
    assert actual == expected
