class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.good_pairs = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.good_pairs += 1

            return [d + 1 for d in left_distances + right_distances]

        dfs(root)
        return self.good_pairs