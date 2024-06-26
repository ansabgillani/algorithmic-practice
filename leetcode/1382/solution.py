# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root: TreeNode) -> TreeNode:
    """
    Balance a given BST by converting it to an in-order list and then constructing a balanced BST from this list.
    
    :param root: The root of the unbalanced binary search tree.
    :return: The root of the balanced binary search tree.
    """
    def inorder_traversal(node):
        if not node:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
    
    def build_balanced_bst(nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = build_balanced_bst(nums, start, mid - 1)
        root.right = build_balanced_bst(nums, mid + 1, end)
        return root
    
    # Perform in-order traversal to get sorted values
    sorted_values = inorder_traversal(root)
    
    # Construct balanced BST from sorted values
    return build_balanced_bst(sorted_values, 0, len(sorted_values) - 1)

# Test cases:
# Example 1: [1,null,2,null,3,null,4,null,null]
root1 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
balanced_root1 = balanceBST(root1)
assert balanced_root1.val == 2 and balanced_root1.left.val == 1 and balanced_root1.right.val == 3 and balanced_root1.right.right.val == 4

# Example 2: [2,1,3]
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
balanced_root2 = balanceBST(root2)
assert balanced_root2.val == 2 and balanced_root2.left.val == 1 and balanced_root2.right.val == 3