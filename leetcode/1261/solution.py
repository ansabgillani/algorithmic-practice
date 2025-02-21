# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered_values = set()
        
        def recover(node, value):
            if node is None:
                return
            node.val = value
            self.recovered_values.add(value)
            recover(node.left, 2 * value + 1)
            recover(node.right, 2 * value + 2)
        
        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.recovered_values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)