class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total_sum = 0
        
        def dfs(node, current_number):
            if not node:
                return
            
            # Append the current node's value to the current number
            current_number = current_number * 10 + node.val
            
            # If it's a leaf node, add the current number to the total sum
            if not node.left and not node.right:
                self.total_sum += current_number
                return
            
            # Recur for left and right children
            dfs(node.left, current_number)
            dfs(node.right, current_number)
        
        dfs(root, 0)
        return self.total_sum