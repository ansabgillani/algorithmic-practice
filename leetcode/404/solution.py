class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        # Check if the left child is a leaf
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        # Recursively sum values of left leaves in both subtrees
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)