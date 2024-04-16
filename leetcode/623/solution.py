# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        queue = [(root, 1)]
        while queue:
            node, current_depth = queue.pop(0)
            if current_depth == depth - 1:
                left_node = TreeNode(val)
                right_node = TreeNode(val)
                left_node.left = node.left
                right_node.right = node.right
                node.left = left_node
                node.right = right_node
            elif current_depth < depth - 1:
                if node.left:
                    queue.append((node.left, current_depth + 1))
                if node.right:
                    queue.append((node.right, current_depth + 1))
        
        return root