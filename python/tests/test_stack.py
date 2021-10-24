from stack_and_queue.stack import Stack
import pytest

def test_push_once():
    """
    Can successfully push onto a stack
    """
    stack=Stack()
    stack.push(1)
    
    actual=stack.top.value
    expected=1
    
    assert actual == expected

def test_push_multiple_values():
    """
    Can successfully push multiple values onto a stack
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push("car")
    
    actual=stack.top.value
    expected="car"
    
    assert actual == expected

def test_pop():
    """
    Can successfully pop off the stack
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push("car")
    
    actual=stack.pop()
    expected="car"
    
    assert actual == expected

def test_pop_to_empty_stack():
    """
    Can successfully empty a stack after multiple pops
    """
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push("car")
    stack.pop()
    stack.pop()
    stack.pop()
    actual=stack.top
    expected=None
    
    assert actual == expected

def test_successfully_peek():
    """
    Can successfully peek the next item on the stack
    """
    stack=Stack()
    stack.push(1)
    
    actual=stack.peek()
    expected=1
    
    assert actual == expected

def test_successfully_instantiate_empty_stack():
    """
    Can successfully instantiate an empty stack
    """
    stack=Stack()
    
    actual=stack.top
    expected=None
    
    assert actual == expected
@pytest.mark.xfail()
def test_pop_empty_stack():
    """
    Calling pop on empty stack raises exception
    """
    stack=Stack()
    stack.pop()
    actual=stack.top
    expected="The stack is empte"
    
    assert actual == expected

@pytest.mark.xfail()
def test_peek_empty_stack():
    """
    Calling peek on empty stack raises exception
    """
    stack=Stack()
    
    actual=stack.peek()
    expected="The stack is empte"
    
    assert actual == expected