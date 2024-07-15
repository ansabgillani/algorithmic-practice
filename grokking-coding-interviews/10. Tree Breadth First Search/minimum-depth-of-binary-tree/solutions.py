# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def minDepth(root: TreeNode) -> int:
    """
    Find the minimum depth of a binary tree.
    
    Args:
    root (TreeNode): The root node of the binary tree.
    
    Returns:
    int: The minimum depth of the binary tree.
    """
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            return depth
        
        # Add left child to the queue if exists
        if node.left:
            queue.append((node.left, depth + 1))
        
        # Add right child to the queue if exists
        if node.right:
            queue.append((node.right, depth + 1))

# Test cases
def test_minDepth():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert minDepth(root) == 2

    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    assert minDepth(root) == 5

test_minDepth()