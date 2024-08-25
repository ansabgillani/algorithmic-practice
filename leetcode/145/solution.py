class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Returns the postorder traversal of a binary tree.
        
        :param root: The root node of the binary tree.
        :return: A list containing the values of the nodes in postorder.
        """
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result[::-1]