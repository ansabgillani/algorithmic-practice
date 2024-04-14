# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    def is_leaf(node):
        return node and not node.left and not node.right
    
    def dfs(node, is_left):
        if not node:
            return 0
        if is_leaf(node) and is_left:
            return node.val
        return dfs(node.left, True) + dfs(node.right, False)
    
    return dfs(root, False)

# Test cases to verify the correctness of the function
def check_solution():
    # Example 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sumOfLeftLeaves(root) == 24
    
    # Example 2
    root = TreeNode(1)
    assert sumOfLeftLeaves(root) == 0

check_solution()