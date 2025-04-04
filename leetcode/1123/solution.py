class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # Helper function to find the depth of a node and its deepest leaf nodes
        def dfs(node):
            if not node:
                return 0, None
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            current_depth = max(left_depth, right_depth) + 1
            
            if left_depth == right_depth:
                return current_depth, node
            elif left_depth > right_depth:
                return current_depth, left_lca
            else:
                return current_depth, right_lca
        
        # Start DFS from the root to find the LCA of the deepest leaves
        _, lca = dfs(root)
        
        return lca