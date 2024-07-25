class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def max_depth(node):
            if not node:
                return 0
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        max_depth(root)
        return self.diameter