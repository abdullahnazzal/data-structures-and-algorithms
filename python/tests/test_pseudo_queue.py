from stack_and_queue.stack_queue_pseudo import PseudoQueue
import pytest

def test_pseudo_queue_enqueue():
    """
    Can successfully enqueue into a Pseudo Queue
    """
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    actual_enqueue_once= queue.first_stack.top.value
    actual_enqueue_second = queue.first_stack.top.next_node.value
    actual_enqueue_third = queue.first_stack.top.next_node.next_node.value
    
    assert actual_enqueue_once == 3
    assert actual_enqueue_second == 2
    assert actual_enqueue_third == 1

@pytest.mark.xfail()
def test_pseudo_queue_enqueue_fail():
    """
    Can't successfully enqueue into a Pseudo Queue
    """
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    actual_enqueue_once= queue.first_stack.top.value
    actual_enqueue_second = queue.first_stack.top.next_node.value
    actual_enqueue_third = queue.first_stack.top.next_node.next_node.value
    
    assert actual_enqueue_once == 1
    assert actual_enqueue_second == 2
    assert actual_enqueue_third == 3

def test_pseudo_queue_dequeue():
    """
    Can successfully dequeue out of a Pseudo Queue the expected value
    """
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    actual_enqueue_once= queue.dequeue()
    actual_enqueue_second = queue.dequeue()
    actual_enqueue_third = queue.dequeue()
    
    assert actual_enqueue_once == 1
    assert actual_enqueue_second == 2
    assert actual_enqueue_third == 3

@pytest.mark.xfail()
def test_pseudo_queue_dequeue_fail():
    """
    Can't successfully dequeue out of a Pseudo Queue the expected value
    """
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    actual_enqueue_once= queue.dequeue()
    actual_enqueue_second = queue.dequeue()
    actual_enqueue_third = queue.dequeue()
    
    assert actual_enqueue_once == 3
    assert actual_enqueue_second == 2
    assert actual_enqueue_third == 1
