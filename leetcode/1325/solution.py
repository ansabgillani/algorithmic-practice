class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # Helper function to perform post-order traversal and delete leaf nodes
        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # If the current node is a leaf node with the target value, return None to remove it
            if not node.left and not node.right and node.val == target:
                return None
            
            return node
        
        # Start the DFS from the root of the tree
        return dfs(root)