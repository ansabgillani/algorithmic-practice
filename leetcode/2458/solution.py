class Solution:
    def treeQueries(self, root: TreeNode, queries: List[int]) -> List[int]:
        depth = {}
        max_depth = {None: -1}

        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            depth[node.val] = 1 + max(left, right)
            max_depth[node.val] = max(max_depth.get(node.parent_val, -1), depth[node.val])
            return depth[node.val]

        def update_max_depth():
            for node in [node for node in depth if node != root.val]:
                max_depth[node.parent_val] = max(max_depth.get(node.parent_val, -1), 
                                                  max(max_depth[node.left], max_depth[node.right]) + 1)

        dfs(root)
        update_max_depth()
        return [max_depth[query] for query in queries]