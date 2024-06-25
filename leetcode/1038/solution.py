class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Helper function to perform reverse in-order traversal and accumulate the sum
        def reverse_inorder(node, total_sum):
            if not node:
                return 0
            
            # Traverse the right subtree first
            right_sum = reverse_inorder(node.right, total_sum)
            
            # Update current node's value with the accumulated sum
            new_val = node.val + right_sum
            node.val = new_val
            
            # Traverse the left subtree and continue accumulating the sum
            return node.val + reverse_inorder(node.left, new_val)
        
        # Start traversal from the root with initial total sum of 0
        reverse_inorder(root, 0)
        return root