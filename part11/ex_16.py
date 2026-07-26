"""
A function named greatest_node(root: Node) which takes the root node of a binary tree as its argument.
The function should return the value of the node with the greatest value within the tree.
The tree should be traversed recursively.
"""

class Node:
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
def greatest_node(root: Node):
    if root is None:
        return float('-inf')

    greatest = root.value

    if root.left_child is not None:
        greatest = max(greatest, greatest_node(root.left_child))

    if root.right_child is not None:
        greatest = max(greatest, greatest_node(root.right_child))

    return greatest
