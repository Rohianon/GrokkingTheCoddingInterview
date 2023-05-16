"""
A cord tree is a binary tree of strings.
A node in this tree can be a leaf node or an internal node.
An internal node has two children, a left child and a right child. It also 
has a length of all the children under it
A leaf nodes have a value and a length
                                      InternalNode, 26
                                      /              \   
                                     /                \                         
                                    /                  \
                                 Leaf(5, ABCDE)      InternalNode, 21
                                                       /           \
                                                      /             \
                                                     /               \
                                                    /                 \
                                         Leaf(10, FGHIJKLMNO)     Leaf(11, PQRSTUVWXYZ)  
"""
# Data Structure to represent the CordTree

# Function that takes in a tree and an index and returns the character at that index
from collections import deque

class CordTree:
    """Root of the tree"""
    def __init__(self, root):
        self.root = root

class InternalNode:
    """Contains two children and their length"""
    def __init__(self, left, right, length):
        self.left = left
        self.right = right
        self.length = length

class LeafNode:
    """Contains the value and the length"""
    def __init__(self, length, value):
        self.length = length
        self.value = value

def find_cord_at_index(tree, index):
    """Return the character at index"""
    if not tree.root: 
        return ""

    queue = deque([tree.root])
    current_index = 0

    while queue:
        node = queue.popleft()
        
        if isinstance(node, InternalNode):
            queue.append(node.left)
            queue.append(node.right)
            continue

        if (current_index + node.length) <= index:
            current_index += node.length
            continue
        
        index_to_return = index - current_index
        
        return node.value[index_to_return]
    
    return ""

if __name__ == "__main__":
    root = InternalNode(LeafNode(5, "ABCDE"), InternalNode(LeafNode(10, "FGHIJKLMNO"), LeafNode(11, "PQRSTUVWXYZ"), 21), 26)
    print(find_cord_at_index(CordTree(root), 4))
