from trees.trees import Node,Binary_Tree

from hashmap.hash_map import HashTable,repeated_word

def tree_intersection(tree1,tree2):
    """
    Find common values in 2 binary trees.
    """
    common =[]
    hash = HashTable()
    # print(tree1.root.value)
    if not tree1.root or not tree2.root:
        return "None"
    def walk(root1):
        hash.add(str(root1.value),root1.value)
        if root1.left:
            walk(root1.left)
        if root1.right:
            walk(root1.right)
    walk(tree1.root)

    def walk2(root2):
        result = hash.contains(str(root2.value))
        if result:
            common.append(root2.value)
        if root2.left:
            walk2(root2.left)
        if root2.right:
            walk2(root2.right)
    walk2(tree2.root)
    return common


if __name__=="__main__":

    tree1 = Binary_Tree()
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(1)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    tree1.root=a_node
    tree1.in_order()
    # --------------------
    tree2 = Binary_Tree()
    a_node = Node(1)
    b_node = Node(1)
    c_node = Node(9)
    d_node = Node(2)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    tree2.root=a_node
    tree2.in_order()

    print(tree_intersection(tree1,tree2))

# Execution Model
# python -m tree_intersection.tree_intersection
