# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Invert the binary tree and return its root.
        
        Args:
        root (TreeNode): The root of the binary tree to be inverted.
        
        Returns:
        TreeNode: The root of the inverted binary tree.
        """
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left subtree
        self.invertTree(root.left)
        
        # Recursively invert the right subtree
        self.invertTree(root.right)
        
        return root

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Construct a sample tree:       4
    #                              / \
    #                             2   7
    #                            / \ / \
    #                           1  3 6  9
    
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    inverted_root = solution.invertTree(root)
    
    # The structure of the inverted tree should be:
    #       4
    #      / \
    #     7   2
    #    / \ / \
    #   9  6 3  1