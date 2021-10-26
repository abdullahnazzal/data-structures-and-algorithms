from stack_and_queue.stack_queue_brackets import validate_brackets
import pytest

def test_match_brackets():
    """
    Can successfully if brackets was matched
    """
    actual_match_brackets_one= validate_brackets("{}")
    actual_match_brackets_second = validate_brackets("{}(){}")
    actual_match_brackets_third= validate_brackets("()[[Extra Characters]]")
    actual_match_brackets_fourth = validate_brackets("(){}[[]]")
    actual_match_brackets_fifth= validate_brackets("{}{Code}[Fellows](())")
    
    assert actual_match_brackets_one == True
    assert actual_match_brackets_second == True
    assert actual_match_brackets_third == True
    assert actual_match_brackets_fourth == True
    assert actual_match_brackets_fifth == True
    
    
    

@pytest.mark.xfail()
def test_match_brackets():
    """
    Can't successfully if brackets was not matched
    """
    actual_match_brackets_one= validate_brackets("{")
    actual_match_brackets_second = validate_brackets("{}({}")
    actual_match_brackets_third= validate_brackets("()[[")
    
    
    
    assert actual_match_brackets_one == True
    assert actual_match_brackets_second == True
    assert actual_match_brackets_third == True
    