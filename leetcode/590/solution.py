class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        # Helper function to perform postorder traversal recursively
        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)
            result.append(node.val)
        
        traverse(root)
        return result

# Example usage:
# root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
# solution = Solution()
# print(solution.postorder(root))  # Output: [5, 6, 3, 2, 4, 1]