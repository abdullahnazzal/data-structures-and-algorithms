# Hashtables

Hash maps are indexed data structures. A hash map makes use of a hash function to compute an index with a key into an array of buckets or slots. Its value is mapped to the bucket with the corresponding index. The key is unique and immutable. Think of a hash map as a cabinet having drawers with labels for the things stored in them. For example, storing user information- consider email as the key, and we can map values corresponding to that user such as the first name, last name etc to a bucket.

## Challenge

Implement a Hashtable Class with the following methods:
add, get, contains, hash

## Approach & Efficiency

Time: O(1)

Space: O(1)

## API

**hash("d")**:
    Arguments: key
    Returns: Index in the collection for that key

**get("d")**:
    Arguments: key
    Returns: Value associated with that key in the table

**add("Abdullah","079")**:
    Arguments: key, value
    Returns: nothing
    This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

**contains("Abdullah")**:
    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.
