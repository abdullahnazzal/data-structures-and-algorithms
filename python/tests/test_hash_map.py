
from hashmap.hash_map import HashTable
import pytest

@pytest.fixture
def hashtable():
	return HashTable()
@pytest.fixture
def hashtable_data(hashtable):
	return hashtable.add("Abdullah","079")

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

def test_add(hashtable):
    """

    """
    hashtable.add("Abdullah","079")
    expected = "079"
    actual = hashtable.get("Abdullah")
    assert actual == expected

def test_get(hashtable_data,hashtable):
    """
    Successfully returns the Value for a key that does exist in the hashtable
    """
    hashtable_data
    expected = "079"
    actual = hashtable.get("Abdullah")
    assert actual == expected

def test_get_None(hashtable_data,hashtable):
    """
    Successfully returns null for a key that does not exist in the hashtable
    """
    hashtable_data
    expected = None
    actual = hashtable.get("Abdullaha")
    assert actual == expected

def test_contains(hashtable_data,hashtable):
    """

    """
    hashtable_data
    expected = True
    actual = hashtable.contains("Abdullah")
    assert actual == expected
