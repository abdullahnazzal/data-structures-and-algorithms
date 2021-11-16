from merge_sort.merge_sort import merge_sort,merge

import pytest
def test_merge_sort():
    """
    Can successfully do merge sort on array
    """
    expected = [4,8,15,16,23,42]
    actual =merge_sort([8,4,23,42,16,15])
    assert actual == expected

@pytest.mark.xfail()
def test_insertion_sort_fail():
    """
    Can't successfully do merge sort on array
    """
    expected = [4,8,15,16,42,23]
    actual =merge_sort([8,4,23,42,16,15])
    assert actual == expected
