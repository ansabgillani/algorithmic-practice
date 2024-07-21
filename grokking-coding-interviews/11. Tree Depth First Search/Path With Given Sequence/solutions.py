class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, arr: List[int], index: int) -> bool:
    # Check if we have reached the end of the array and it matches with the current node's value
    if not root or index == len(arr):
        return False
    # Check if the current node's value matches the element in the array at the current index
    if root.val != arr[index]:
        return False
    # If we are at the last element of the array, check if it is a leaf node
    if index == len(arr) - 1:
        return not root.left and not root.right
    # Recursively check the left and right subtrees
    return hasPathSum(root.left, arr, index + 1) or hasPathSum(root.right, arr, index + 1)

# Example usage:
# Constructing the binary tree from the example input
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

arr1 = [5, 2, 4, 8]
print(hasPathSum(root, arr1, 0))  # Output: True

arr2 = [5, 3, 4, 9]
print(hasPathSum(root, arr2, 0))  # Output: False