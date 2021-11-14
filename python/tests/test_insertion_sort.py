from insertion_sort.insertion_sort import insertion_sort

import pytest
def test_insertion_sort():
    """
    Can successfully do insertion sort on array
    """
    expected = [4,8,15,16,23,42]
    actual =insertion_sort([8,4,23,42,16,15])
    assert actual == expected

@pytest.mark.xfail()
def test_insertion_sort_fail():
    """
    Can successfully do insertion sort on array
    """
    expected = [4,8,15,16,42,23]
    actual =insertion_sort([8,4,23,42,16,15])
    assert actual == expected
