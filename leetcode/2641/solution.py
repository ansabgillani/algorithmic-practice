class Solution:
    def replaceValueInTree(self, root: 'TreeNode') -> 'TreeNode':
        depth_sum = defaultdict(int)
        parent_depth = defaultdict(lambda: -1)

        def dfs(node, depth=0):
            if not node:
                return 0
            parent_depth[node] = depth
            depth_sum[depth] += node.val
            return dfs(node.left, depth + 1) + dfs(node.right, depth + 1) + 1

        total_nodes = dfs(root)

        def bfs():
            q = deque([root])
            while q:
                size = len(q)
                for i in range(size):
                    node = q.popleft()
                    if parent_depth[node] == -1:
                        node.val = total_nodes - node.val
                    else:
                        cousin_sum = depth_sum[parent_depth[node]] - (node.left.val + node.right.val if node.left and node.right else 0)
                        node.val = cousin_sum

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        bfs()
        
        return root