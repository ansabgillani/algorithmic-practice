class Solution:
    def isSubPath(self, head, root):
        if not head:
            return True
        if not root:
            return False

        def dfs(node, current):
            if not current.next:
                return True
            if node.val == current.next.val:
                return dfs(node.left, current.next) or dfs(node.right, current.next)
            else:
                return False

        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)