from quick_sort.quick_sort import quick_sort

import pytest
def test_quick_sort():
    """
    Can successfully do quick sort on array
    """
    expected = [4,8,15,16,23,42]
    array= [4,8,15,16,23,42]
    actual =quick_sort(array, 0 , len(array) - 1)
    assert actual == expected

@pytest.mark.xfail()
def test_insertion_sort_fail():
    """
    Can't successfully do quick sort on array
    """
    expected = [4,8,15,16,42,23]
    array= [4,8,15,16,23,42]
    actual =quick_sort(array, 0 , len(array) - 1)
    assert actual == expected
