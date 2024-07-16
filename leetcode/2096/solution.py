class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Helper function to find the path from root to a target value
        def find_path(node, target):
            if not node:
                return None
            
            if node.val == target:
                return []
            
            left = find_path(node.left, target)
            if left is not None:
                left.append('L')
                return left
            
            right = find_path(node.right, target)
            if right is not None:
                right.append('R')
                return right
            
            return None
        
        # Find paths from root to startValue and destValue
        path_to_start = find_path(root, startValue)
        path_to_dest = find_path(root, destValue)
        
        # Determine the lowest common ancestor (LCA)
        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1
        
        # Convert paths to required format
        up_steps = 'U' * (len(path_to_start) - i)
        dest_steps = ''.join(reversed(path_to_dest[i:]))
        
        return up_steps + dest_steps