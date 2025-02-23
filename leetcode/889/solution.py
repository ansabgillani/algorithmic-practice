# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Reconstructs a binary tree from given preorder and postorder traversals.
        
        :param preorder: List[int] - Preorder traversal of the binary tree
        :param postorder: List[int] - Postorder traversal of the binary tree
        :return: TreeNode - Root of the reconstructed binary tree
        """
        if not preorder or not postorder:
            return None
        
        # The first element in preorder is the root
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        # Find the index of the second element in preorder which will be the left child
        for i in range(1, len(postorder)):
            if postorder[i] == preorder[1]:
                break
        
        # Recursively construct the left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:i+2], postorder[:i+1])
        root.right = self.constructFromPrePost(preorder[i+2:], postorder[i+1:-1])
        
        return root