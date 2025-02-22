class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, i = [], 0
        while i < len(traversal):
            depth = 0
            while traversal[i] == '-':
                depth += 1
                i += 1
            value = ''
            while i < len(traversal) and traversal[i].isdigit():
                value += traversal[i]
                i += 1
            node = TreeNode(int(value))
            while len(stack) > depth:
                stack.pop()
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]