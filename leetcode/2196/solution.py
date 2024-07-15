# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions):
    # Dictionary to store nodes by their value
    nodes = {}
    # Set to keep track of child nodes
    children = set()
    
    for parent, child, isLeft in descriptions:
        # Create or get the parent node
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        # Create or get the child node
        if child not in nodes:
            nodes[child] = TreeNode(child)
        children.add(child)
        
        # Assign the child to the parent's left or right child
        if isLeft == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
    
    # Find the root node (the only one that is not a child)
    for node in nodes.values():
        if node.val not in children:
            return node

# Example usage:
# descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# root = createBinaryTree(descriptions)