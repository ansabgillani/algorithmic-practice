class Solution:
    def balanceBST(self, root):
        # Helper function to perform inorder traversal and collect nodes in sorted order
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
        
        # Helper function to build a balanced BST from the sorted list of nodes
        def build_balanced_bst(nodes, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = build_balanced_bst(nodes, start, mid - 1)
            node.right = build_balanced_bst(nodes, mid + 1, end)
            return node
        
        # Step 1: Perform inorder traversal to get nodes in sorted order
        sorted_nodes = inorder_traversal(root)
        
        # Step 2: Build a balanced BST from the sorted list of nodes
        return build_balanced_bst(sorted_nodes, 0, len(sorted_nodes) - 1)