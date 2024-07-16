class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getPath(node, val):
            if not node:
                return None
            if node.val == val:
                return []
            left = getPath(node.left, val)
            if left is not None:
                return ['L'] + left
            right = getPath(node.right, val)
            if right is not None:
                return ['R'] + right
            return None

        pathStart = getPath(root, startValue)
        pathDest = getPath(root, destValue)

        i = 0
        while i < len(pathStart) and i < len(pathDest) and pathStart[i] == pathDest[i]:
            i += 1

        upPath = ['U'] * (len(pathStart) - i)
        downPath = pathDest[i:]

        return ''.join(upPath + downPath)

# Example usage:
# root = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, None, TreeNode(6, TreeNode(4))))
# solution = Solution()
# print(solution.getDirections(root, 3, 6))  # Output: "UURL"