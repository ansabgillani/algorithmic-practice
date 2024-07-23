# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    """
    Returns the maximum path sum of any non-empty path in a binary tree.
    
    :param root: Root node of the binary tree.
    :return: The maximum path sum.
    """
    result = float('-inf')
    
    def max_gain(node):
        nonlocal result
        if not node:
            return 0
        
        # Recursively find the max gain from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Price to start a new path where `node` is the highest node
        price_newpath = node.val + left_gain + right_gain
        
        # Update max_sum if it's better to start a new path
        result = max(result, price_newpath)
        
        # For recursion :
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return result

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# print(maxPathSum(root))  # Output: 6