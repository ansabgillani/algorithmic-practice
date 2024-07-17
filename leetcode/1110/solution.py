# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    # Helper function to perform DFS and delete nodes
    def dfs(node, parent_deleted):
        if not node:
            return None
        
        # Recursively delete child nodes
        node.left = dfs(node.left, False)
        node.right = dfs(node.right, False)
        
        # If current node needs to be deleted
        if node.val in to_delete_set:
            if parent_deleted:
                return None  # No need to add this node to the result
            
            # Add left and right children (if they exist) to the result
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
            return None  # Remove current node from parent
        
        return node
    
    to_delete_set = set(to_delete)
    res = []
    
    # Start DFS with a dummy node as the parent of the root
    dummy = TreeNode(-1)
    dummy.left = root
    dfs(dummy, True)
    
    if root.val not in to_delete_set:
        res.append(root)
    
    return res