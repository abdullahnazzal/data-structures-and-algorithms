"""
The implementation of Node class, Linked list class, and Hashmap class.
"""


import re


class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
        """
        Retrieve the most recent value of in oour hasmap for the given key

        :param key str
        :rvalue any
        """
        # calculate index
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self.__buckets[index]:
            # iterate over linked list
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                # check if the key in each node matches
                if current.value[0] == key:
                    # return the value of the node with the mathcing key
                    return current.value[1]
                current = current.next

        # return None
        return None

    def contains(self, key):
        """
        Indicating if the key exists in the table already.

        :param key str
        :returns boolean
        """
        # calculate index
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self.__buckets[index]:
            # iterate over linked list
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                # check if the key in each node matches
                if current.value[0] == key:
                    # return the value of the node with the mathcing key
                    return True
                current = current.next

        # return None
        return False

def repeated_word(words):
    arr = re.sub("[^\w' ]",'',words).lower().split(" ")
    hash = HashTable()
    for i in arr:
        if hash.contains(i):
            return i
        hash.add(i,i)
    return "None"

def unique_characters(words):
    words = words.replace(" ","").lower()
    arr = [char for char in words]
    hash = HashTable()
    for i in arr:
        if hash.contains(i):
            return False
        hash.add(i,i)
    return True

# x=unique_characters("I love catS")
# print(x)

def common_word(words):
    arr = re.sub("[^\w' ]",'',words).lower().split(" ")
    hash = HashTable()
    counter = {}
    for i in arr:
        print(i)
        if hash.contains(i):
            if i in counter:
                counter[i] += 1
            else:
                counter[i]=1
        hash.add(i,i)
    print(counter)
    return "None"

def left_join(map1,map2):
    """

    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
    """
    if  not len(map1._HashTable__buckets)  and not len(map1._HashTable__buckets) :
        return []
    arr = []
    for i in range(len(map1._HashTable__buckets)):
        if map1._HashTable__buckets[i]:
            if map2.contains(map1._HashTable__buckets[i].head.value[0]):
                arr.append([map1._HashTable__buckets[i].head.value[0],map2._HashTable__buckets[i].head.value[1],map1._HashTable__buckets[i].head.value[1]])
            else:
                arr.append([map1._HashTable__buckets[i].head.value[0],map2._HashTable__buckets[i].head.value[1],None])
    return arr

# ht1 = HashTable()
# ht1.add("hi","h")
# ht1.add("hello","he")
# ht2 = HashTable()
# ht2.add("hi","hh")
# ht2.add("hello","hel")
# x = left_join(ht1,ht2)
# print(x)
# x=common_word("Once upon a time, there was a brave upon a princess who...")
# print(x)
# x=repeated_word("Once upon a time, there was a brave princess who...")
# print(x)
# h = HashTable()
# print(h._HashTable__hash("d"))
# h.add("cloud","00")
# h.add("could","00")

# h.add("Abdullah","079")
# print(h.get("could"))
# h.get("Abdullah")
# print(h.contains("cloud"))

# # h.get("Abdullah")
# h.add("Abdullah","079")
# h.add("Ahmad","079")
# h.add("Ali","079")
# h.add("Khalad","079")
# h.add("Dairio","079")
# print(h._HashTable__buckets)
