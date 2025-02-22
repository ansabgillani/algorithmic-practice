class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(traversal: str) -> TreeNode:
    stack = []
    i = 0
    while i < len(traversal):
        level = 0
        # Determine the depth of the current node
        while i < len(traversal) and traversal[i] == '-':
            level += 1
            i += 1
        
        value = 0
        # Determine the value of the current node
        while i < len(traversal) and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1
        
        # Create the current node
        node = TreeNode(value)
        
        # Adjust stack to maintain correct parent-child relationship
        while len(stack) > level:
            stack.pop()
        
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        
        stack.append(node)
    
    return stack[0]