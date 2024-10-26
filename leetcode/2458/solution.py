# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        from collections import defaultdict
        
        # Helper function to get the height of a node
        def getHeight(node):
            if not node:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        # Dictionary to store heights and positions of nodes
        heights = defaultdict(int)
        
        # Helper function to traverse the tree and compute heights
        def dfs(node, depth):
            if not node:
                return -1
            depths[node.val] = depth
            left_height = dfs(node.left, depth + 1)
            right_height = dfs(node.right, depth + 1)
            height = max(left_height, right_height) + 1
            heights[node.val] = height
            return height
        
        # Perform DFS to compute depths and heights of all nodes
        depths = {}
        dfs(root, 0)
        
        # Dictionary to store the maximum height of any subtree rooted at a node's parent
        max_heights = defaultdict(int)
        
        # Helper function to traverse the tree in reverse to compute max heights of subtrees
        def reverseDfs(node):
            if not node:
                return -1
            left_max = reverseDfs(node.left)
            right_max = reverseDfs(node.right)
            parent_height = max(left_max, right_max) + 1
            max_heights[node.val] = parent_height
            return parent_height
        
        # Perform reverse DFS to compute max heights of subtrees for all nodes
        reverseDfs(root)
        
        # Answer array to store the result for each query
        answer = []
        
        # Process each query
        for q in queries:
            original_height = heights[q]
            parent_height = max_heights[depths[q]]
            answer.append(parent_height + original_height - 1)
            
        return answer