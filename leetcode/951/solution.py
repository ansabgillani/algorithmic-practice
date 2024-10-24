class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        # Base case: if both nodes are None, they are equivalent
        if not root1 and not root2:
            return True
        # If one of the nodes is None or their values are different, they are not equivalent
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # Check if the subtrees are equivalent without flipping or with flipping
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        # The trees are equivalent if either no flipping or flipping is valid
        return no_flip or flip

# Example usage:
# tree1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
# tree2 = TreeNode(1, left=TreeNode(3), right=TreeNode(2))
# print(Solution().flipEquiv(tree1, tree2))  # Output: True