class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root: TreeNode) -> bool:
    """
    Evaluate a boolean binary tree.
    
    Args:
    root (TreeNode): The root of the full binary tree.
    
    Returns:
    bool: The boolean result of evaluating the root node.
    """
    # Base case: if it's a leaf node, return its value
    if not root.left and not root.right:
        return root.val == 1
    
    # Recursive case: evaluate left and right children
    left_result = evaluateTree(root.left)
    right_result = evaluateTree(root.right)
    
    # Apply the boolean operation based on the node's value
    if root.val == 2:  # OR operation
        return left_result or right_result
    elif root.val == 3:  # AND operation
        return left_result and right_result

# Example usage:
# root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
# print(evaluateTree(root))  # Output: True