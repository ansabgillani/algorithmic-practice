class Solution:
    def smallestFromLeaf(self, root):
        if not root:
            return ""

        def dfs(node, path):
            current_char = chr(ord('a') + node.val)
            path = current_char + path
            
            if not node.left and not node.right:
                self.min_path = min(self.min_path, path) if self.min_path else path
                return
            
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        self.min_path = ""
        dfs(root, "")
        return self.min_path