from stack_and_queue.stack_queue_animal_shelter import AnimalShelter,Cat,Dog
import pytest

def test_animal_shelter_enqueue():
    """
    Can successfully enqueue into a cat or dog Queue
    """
    shelter=AnimalShelter()
    cat1=Cat("cat1")
    cat2=Cat("cat2")
    dog1=Dog("dog1")
    dog2=Dog("dog2")
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    
    
    actual_enqueue_cat_once= shelter.cat.front.value
    actual_enqueue_cat_second = shelter.cat.rear.value
    actual_enqueue_dog_once= shelter.dog.front.value
    actual_enqueue_dog_second = shelter.dog.rear.value
    assert actual_enqueue_cat_once == "cat1"
    assert actual_enqueue_cat_second == "cat2"
    assert actual_enqueue_dog_once == "dog1"
    assert actual_enqueue_dog_second == "dog2"
    

@pytest.mark.xfail()
def test_animal_shelter_enqueue_fail():
    """
    Can't successfully enqueue into a Cat or Dog Queue
    """
    shelter=AnimalShelter()
    cat1=Cat("cat1")
    cat2=Cat("cat2")
    dog1=Dog("dog1")
    dog2=Dog("dog2")
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    
    
    actual_enqueue_cat_once= shelter.cat.front.value
    actual_enqueue_cat_second = shelter.cat.rear.value
    actual_enqueue_dog_once= shelter.dog.front.value
    actual_enqueue_dog_second = shelter.dog.rear.value
    assert actual_enqueue_cat_once == "cat2"
    assert actual_enqueue_cat_second == "cat1"
    assert actual_enqueue_dog_once == "dog2"
    assert actual_enqueue_dog_second == "dog1"

def test_animal_shelter_dequeue():
    """
    Can successfully dequeue out of a Cat or Dog Queue the expected value
    """
    shelter=AnimalShelter()
    cat1=Cat("cat1")
    cat2=Cat("cat2")
    dog1=Dog("dog1")
    dog2=Dog("dog2")
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    
    
    actual_enqueue_cat_once= shelter.dequeue("cat")
    actual_enqueue_cat_second = shelter.dequeue("cat")
    actual_enqueue_dog_once= shelter.dequeue("dog")
    actual_enqueue_dog_second = shelter.dequeue("dog")
    assert actual_enqueue_cat_once == "cat1"
    assert actual_enqueue_cat_second == "cat2"
    assert actual_enqueue_dog_once == "dog1"
    assert actual_enqueue_dog_second == "dog2"

@pytest.mark.xfail()
def test_animal_shelter_dequeue_fail():
    """
    Can't successfully dequeue out of a Cat or Dog Queue the expected value
    """
    shelter=AnimalShelter()
    cat1=Cat("cat1")
    cat2=Cat("cat2")
    dog1=Dog("dog1")
    dog2=Dog("dog2")
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    
    
    actual_enqueue_cat_once= shelter.dequeue("cat")
    actual_enqueue_cat_second = shelter.dequeue("cat")
    actual_enqueue_dog_once= shelter.dequeue("dog")
    actual_enqueue_dog_second = shelter.dequeue("dog")
    assert actual_enqueue_cat_once == "cat2"
    assert actual_enqueue_cat_second == "cat1"
    assert actual_enqueue_dog_once == "dog2"
    assert actual_enqueue_dog_second == "dog1"
