class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def createBinaryTree(self, descriptions):
        node_map = {}
        parent_set = set()
        child_set = set()
        
        for parent, child, isLeft in descriptions:
            if parent not in node_map:
                node_map[parent] = Solution.TreeNode(parent)
            if child not in node_map:
                node_map[child] = Solution.TreeNode(child)
            
            if isLeft == 1:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
            
            parent_set.add(parent)
            child_set.add(child)
        
        root_val = (parent_set - child_set).pop()
        return node_map[root_val]