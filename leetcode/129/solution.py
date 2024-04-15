class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            path = path * 10 + node.val
            
            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return path
            
            # Recursively sum up all left and right subtrees
            return dfs(node.left, path) + dfs(node.right, path)

        # Start DFS from the root with an initial path of 0
        return dfs(root, 0)