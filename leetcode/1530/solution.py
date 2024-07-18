class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_leaves = dfs(node.left)
            right_leaves = dfs(node.right)
            
            for left in left_leaves:
                for right in right_leaves:
                    if left + right <= distance:
                        self.count += 1
            
            return [i + 1 for i in left_leaves + right_leaves]
        
        dfs(root)
        return self.count