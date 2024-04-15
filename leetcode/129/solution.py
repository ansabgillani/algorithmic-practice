class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Helper function to perform DFS and calculate the sum of numbers from root to leaf
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val
            if not node.left and not node.right:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start DFS from the root with an initial sum of 0
        return dfs(root, 0)