# Trees

A tree data structure can be defined recursively as a collection of nodes, where each node is a data structure consisting of a value and a list of references to nodes. The start of the tree is the "root node" and the reference nodes are the "children". No reference is duplicated and none points to the root.

## Challenge

Impelemt Binary Tree and Binary Search Tree

## Approach & Efficiency

Big (O):
Time --> O(n)
Space --> O(1)

## API

Binary Tree:

    pre order:

    Depth first traversal is where we prioritize going through the depth (height) of the tree first.
    root >> left >> right
    which returns an array of the values, ordered appropriately.

    in order:

    Depth first traversal is where we prioritize going through the depth (height) of the tree first.
    left >> root >> right
    which returns an array of the values, ordered appropriately.

    post order:

    Depth first traversal is where we prioritize going through the depth (height) of the tree first.
    left >> right >> root
    which returns an array of the values, ordered appropriately.

Binary Search Tree:

    Add:

    Adds a new node with that value in the correct location in the binary search tree.

    Contains:

    Return sboolean indicating whether or not the value is in the tree at least once.
