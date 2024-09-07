# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubPath(head: ListNode, root: TreeNode) -> bool:
    
    # Helper function to check if list matches from current tree node
    def dfs(node, head):
        if not head:
            return True
        if not node:
            return False
        if node.val == head.val:
            return dfs(node.left, head.next) or dfs(node.right, head.next)
        return False
    
    # Main function to traverse the tree and check for subpath
    def traverse(root):
        if not root:
            return False
        return dfs(root, head) or traverse(root.left) or traverse(root.right)
    
    return traverse(root)

# Example usage:
# head = ListNode(4, ListNode(2, ListNode(8)))
# root = TreeNode(1, TreeNode(4), TreeNode(4, None, TreeNode(2, None, TreeNode(6))))
# print(isSubPath(head, root))  # Output: True