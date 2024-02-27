# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Returns the length of the longest path between any two nodes in a tree.
        
        The diameter is calculated as the sum of heights of the left and right subtrees,
        considering that the path may or may not pass through the root.
        
        :param root: The root node of the binary tree
        :return: The diameter of the binary tree
        """
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1
        
        if not root:
            return 0
        
        left_height = height(root.left)
        right_height = height(root.right)
        
        return max(left_height + right_height, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))