
from hashmap.hash_map import HashTable,left_join
import pytest

@pytest.fixture
def hashtable1():
    ht1 = HashTable()
    ht1.add("hi","h")
    ht1.add("hello","he")
    return ht1

@pytest.fixture
def hashtable2():
    ht2 = HashTable()
    ht2.add("hi","hh")
    ht2.add("hello","hel")
    return ht2

def test_left_join(hashtable1,hashtable2):
    """
    Successfully returns joined two hash map
    """
    actual = left_join(hashtable1,hashtable2)
    expected = [['hi', 'hh', 'h'], ['hello', 'hel', 'he']]
    print(actual)
    assert actual == expected
