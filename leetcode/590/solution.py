class Solution:
    def postorder(self, root):
        if root is None:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.children:
                stack.extend(node.children)
        
        return result[::-1]