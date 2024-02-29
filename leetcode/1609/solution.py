# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = deque([root])
        level = 0
        
        while queue:
            prev_val = None
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # Check even-indexed level conditions
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                # Check odd-indexed level conditions
                else:
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False
                
                prev_val = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True