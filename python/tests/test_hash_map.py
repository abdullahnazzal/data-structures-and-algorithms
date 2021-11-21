
from hashmap.hash_map import HashTable,repeated_word
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
    Successfully add key and Value pair in the hashtable.
    """
    hashtable.add("Abdullah","079")
    expected = "079"
    actual = hashtable.get("Abdullah")
    assert actual == expected

def test_get(hashtable_data,hashtable):
    """
    Successfully returns the Value for a key that does exist in the hashtable.
    """
    hashtable_data
    expected = "079"
    actual = hashtable.get("Abdullah")
    assert actual == expected

def test_get_None(hashtable_data,hashtable):
    """
    Successfully returns null for a key that does not exist in the hashtable.
    """
    hashtable_data
    expected = None
    actual = hashtable.get("Abdullaha")
    assert actual == expected

def test_contains(hashtable_data,hashtable):
    """
    Successfully returns the True if there key in hashmap.
    """
    hashtable_data
    expected = True
    actual = hashtable.contains("Abdullah")
    assert actual == expected

def test_contains():
    """
    Successfully returns the first word to occur more than once in a string.
    """
    words1 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness,"
    expected1 = "it"
    actual1 = repeated_word(words1)
    words2 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    expected2 = "summer"
    actual2 = repeated_word(words2)
    assert actual1 == expected1
    assert actual2 == expected2
