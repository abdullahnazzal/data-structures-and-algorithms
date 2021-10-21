from stack_and_queue.queue import Queue
import pytest

def test_enqueue_once():
    """
    Can successfully enqueue into a queue
    """
    queue=Queue()
    queue.enqueue(1)
    
    actual=queue.rear.value
    expected=1
    
    assert actual == expected

def test_enqueue_multiple_values():
    """
    Can successfully enqueue multiple values into a queue
    """
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("car")
    
    actual=queue.rear.value
    expected="car"
    
    assert actual == expected

def test_enqueue():
    """
    Can successfully dequeue out of a queue the expected value
    """
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("car")
    
    actual=queue.dequeue()
    expected=1
    
    assert actual == expected

def test_successfully_peek():
    """
    Can successfully peek into a queue, seeing the expected value
    """
    queue=Queue()
    queue.enqueue(1)
    
    actual=queue.peek()
    expected=1
    
    assert actual == expected

def test_dequeue_to_empty_stack():
    """
    Can successfully empty a queue after multiple dequeues
    """
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("car")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual=queue.front
    expected=None
    
    assert actual == expected



def test_successfully_instantiate_empty_stack():
    """
    Can successfully instantiate an empty queue
    """
    queue=Queue()
    
    actual=queue.front
    expected=None
    
    assert actual == expected
@pytest.mark.xfail()
def test_dequeue_empty_queue():
    """
    Calling dequeue or peek on empty queue raises exception
    """
    queue=Queue()
    # queue.dequeue()
    actual=queue.dequeue()
    expected="The queue is empty"
    
    assert actual == expected

@pytest.mark.xfail()
def test_peek_empty_queue():
    """
    Calling peek on empty queue raises exception
    """
    queue=Queue()
    
    actual=queue.peek()
    expected="The queue is empty"
    
    assert actual == expected