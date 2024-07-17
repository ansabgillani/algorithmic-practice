class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete_set:
                if node.left: 
                    result.append(node.left)
                if node.right: 
                    result.append(node.right)
                return None
            else:
                return node

        dfs(root)

        if root and root.val not in to_delete_set:
            result.append(root)
        
        return result