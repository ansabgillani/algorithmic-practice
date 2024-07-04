from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Returns the level order traversal of a binary tree.
        
        :param root: The root node of the binary tree.
        :return: A list of lists containing the values of nodes at each level.
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result