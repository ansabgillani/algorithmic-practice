# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node at this level, add its value to the result
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    root1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, right=TreeNode(4)))
    print(sol.rightSideView(root1))  # Output: [1, 3, 4]
    
    # Example 2
    root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(sol.rightSideView(root2))  # Output: [1, 3, 4, 5]
    
    # Example 3
    root3 = TreeNode(1, right=TreeNode(3))
    print(sol.rightSideView(root3))  # Output: [1, 3]
    
    # Example 4
    root4 = None
    print(sol.rightSideView(root4))  # Output: []