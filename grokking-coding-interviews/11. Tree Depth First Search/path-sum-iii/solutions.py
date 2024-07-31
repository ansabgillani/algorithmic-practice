# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0
        
        def dfs(node, current_sum):
            if node is None:
                return
            current_sum += node.val
            if current_sum == targetSum:
                self.count += 1
            
            # Check paths in the left and right subtrees
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        def traverse(root):
            if root is None:
                return
            dfs(root, 0)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.count

# Example usage:
# root = TreeNode(10, TreeNode(5), TreeNode(-3))
# root.left.left = TreeNode(3, TreeNode(3), TreeNode(-2))
# root.left.right = TreeNode(2, None, TreeNode(1))
# root.right.right = TreeNode(11)
# print(Solution().pathSum(root, 8))  # Output: 3