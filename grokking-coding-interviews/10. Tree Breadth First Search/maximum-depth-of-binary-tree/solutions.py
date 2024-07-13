# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Returns the maximum depth of a binary tree.
        
        :param root: The root node of the binary tree
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1

# Test cases to verify the solution
def test_maxDepth():
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().maxDepth(root) == 3
    
    # Example 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().maxDepth(root) == 2

# Run the test cases
test_maxDepth()