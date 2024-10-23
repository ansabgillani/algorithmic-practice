# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def replaceValueInTree(root: TreeNode) -> TreeNode:
    # Initialize the root value to 0 as it has no cousins.
    if not root:
        return None
    
    queue = [(root, -1)]
    level_sum = {None: 0}
    
    while queue:
        size = len(queue)
        next_level = []
        
        for _ in range(size):
            node, parent_val = queue.pop(0)
            
            # Sum of all nodes at the current level.
            level_sum[parent_val] += node.val
            
            if node.left:
                next_level.append((node.left, node.val))
            if node.right:
                next_level.append((node.right, node.val))
        
        queue = next_level
    
    def dfs(node, parent_val):
        if not node:
            return
        
        # Calculate the sum of cousins by subtracting the current node's value and its parent's value from the total level sum.
        cousin_sum = level_sum[parent_val] - node.val
        node.val = cousin_sum
        
        if node.left:
            dfs(node.left, node.val)
        if node.right:
            dfs(node.right, node.val)
    
    # Start DFS from the root with a parent value of -1 (no parent).
    dfs(root, -1)
    
    return root