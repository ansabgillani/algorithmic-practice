class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def helper(node: TreeNode) -> None:
            if node:
                helper(node.right)
                self.sum += node.val
                node.val = self.sum
                helper(node.left)
        
        helper(root)
        return root