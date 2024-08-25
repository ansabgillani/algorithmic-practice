class Solution:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def postorderTraversal(self, root: 'TreeNode') -> List[int]:
        result = []
        
        # Helper function for recursion
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)
        
        dfs(root)
        return result