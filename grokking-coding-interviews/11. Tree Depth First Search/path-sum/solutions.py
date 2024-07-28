class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: if the current node is None, there's no path
        if not root:
            return False
        
        # Update the target sum by subtracting the current node's value
        targetSum -= root.val
        
        # Check if we have reached a leaf node and the target sum is zero
        if not root.left and not root.right and targetSum == 0:
            return True
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)