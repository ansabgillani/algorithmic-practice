# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = [root]
        level = 0
        
        while queue:
            if level % 2 == 1:
                # Reverse the values at this odd level
                for i in range(len(queue) // 2):
                    queue[i].val, queue[~i].val = queue[~i].val, queue[i].val
            
            # Prepare the next level
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            
            queue = new_queue
            level += 1
        
        return root

# Test cases
if __name__ == "__main__":
    def build_tree(nodes):
        if not nodes or nodes[0] is None:
            return None
        root = TreeNode(nodes[0])
        q = [root]
        i = 1
        while q and i < len(nodes):
            node = q.pop(0)
            if nodes[i]:
                node.left = TreeNode(nodes[i])
                q.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i]:
                node.right = TreeNode(nodes[i])
                q.append(node.right)
            i += 1
        return root
    
    def print_tree(root):
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res

    # Example 1
    root1 = build_tree([2,3,5,8,13,21,34])
    solution = Solution().reverseOddLevels(root1)
    print(print_tree(solution))  # Expected: [[2], [5, 3], [34, 21, 13, 8]]

    # Example 2
    root2 = build_tree([7,13,11])
    solution = Solution().reverseOddLevels(root2)
    print(print_tree(solution))  # Expected: [[7], [11, 13]]
    
    # Example 3
    root3 = build_tree([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])
    solution = Solution().reverseOddLevels(root3)
    print(print_tree(solution))  # Expected: [[0], [2, 1], [1, 1, 2, 2]]