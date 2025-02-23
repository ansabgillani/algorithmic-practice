class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder.pop(0)
        node = TreeNode(root_val)
        
        if preorder:
            left_root_val = preorder[0]
            left_index_in_postorder = postorder.index(left_root_val)
            
            if left_index_in_postorder == 0:
                node.left = None
            else:
                node.left = self.constructFromPrePost(preorder, postorder[:left_index_in_postorder+1])
            
            if preorder:
                node.right = self.constructFromPrePost(preorder, postorder[left_index_in_postorder:-1])
        
        return node