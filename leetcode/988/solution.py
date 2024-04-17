# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, path):
            if not node:
                return None
            # Convert node value to corresponding character and add to the front of the path
            char = chr(ord('a') + node.val)
            new_path = char + path
            
            # If it's a leaf node, return the current path
            if not node.left and not node.right:
                return new_path
            
            # Recursively find the smallest string from left and right children
            left_result = dfs(node.left, new_path)
            right_result = dfs(node.right, new_path)
            
            # If one of the results is None, return the other
            if left_result is None:
                return right_result
            elif right_result is None:
                return left_result
            
            # Return the lexicographically smaller string
            return min(left_result, right_result)
        
        return dfs(root, "")