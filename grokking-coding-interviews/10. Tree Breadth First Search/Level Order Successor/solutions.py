class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderSuccessor(root, target):
    if not root or not target:
        return None
    
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        
        if current == target:
            # Check if there is a next node in the queue
            if queue:
                return queue[0]
            else:
                return None
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return None

# Test cases
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(26)
root.left.left = TreeNode(4)
root.left.right = TreeNode(18)
root.right.left = TreeNode(24)
root.right.right = TreeNode(27)
root.left.right.left = TreeNode(14)
root.left.right.right = TreeNode(19)
root.left.right.left.left = TreeNode(13)
root.left.right.left.right = TreeNode(15)

# Example 1
print(levelOrderSuccessor(root, root.right.left).val)  # Output: 27

# Example 2
print(levelOrderSuccessor(root, root.left.left).val)  # Output: 18