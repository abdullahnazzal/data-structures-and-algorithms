class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=None
class Queue:
    
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next_node=node
            self.rear=node
    
    def dequeue(self):
        """
        Returns: the value from node from the front of the queue.
        Removes the node from the front of the queue.
        Should raise exception when called on empty queue.
        """
        if self.front:
            temp=self.front
            self.front=self.front.next_node
            temp.next_node=None
            return temp.value
        else:
            raise Exception("The queue is empty")
    
            
class Dog:
    def __init__(self,name):
        self.name=name
        self.kind="dog"

class Cat:
    def __init__(self,name):
        self.name=name
        self.kind="cat"

class AnimalShelter:

    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()
    
    def enqueue(self,animal):
        """
        Arguments: animal
        animal can be either a dog or a cat object.
        """
        if animal.kind=="cat":
            self.cat.enqueue(animal.name)
            
        elif animal.kind=="dog":
            self.dog.enqueue(animal.name)
            
        
    def dequeue(self,pref):
        """
        Arguments: pref
        pref can be either "dog" or "cat"
        Return: either a dog or a cat, based on preference.
        If pref is not "dog" or "cat" then return null
        """
        if pref == "cat":
            return self.cat.dequeue()
        elif pref == "dog":
            return self.dog.dequeue()
        else:
            return None

shelter=AnimalShelter()
cat1=Cat("cat1")
cat2=Cat("cat2")
dog1=Dog("dog1")
dog2=Dog("dog2")
shelter.enqueue(cat1)
shelter.enqueue(cat2)
print(shelter.dequeue("cat"))
print(shelter.dequeue("cat"))
shelter.enqueue(dog1)
shelter.enqueue(dog2)
print(shelter.dequeue("dog"))
print(shelter.dequeue("dog"))
