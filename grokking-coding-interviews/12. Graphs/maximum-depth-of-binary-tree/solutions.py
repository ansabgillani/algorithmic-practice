class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    """
    Calculate the maximum depth of a binary tree.
    
    Args:
    root (TreeNode): The root node of the binary tree.
    
    Returns:
    int: The maximum depth of the binary tree.
    """
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

# Test cases
def test_maxDepth():
    # Example 1
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert maxDepth(root1) == 3
    
    # Example 2
    root2 = TreeNode(1, None, TreeNode(2))
    assert maxDepth(root2) == 2

# Run tests
test_maxDepth()