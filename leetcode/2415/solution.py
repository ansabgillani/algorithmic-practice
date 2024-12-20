class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        
        queue = [root]
        level = 0
        
        while queue:
            size = len(queue)
            temp = []
            
            for i in range(size):
                node = queue.pop(0)
                
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    
                    if level % 2 != 0:
                        temp.append(node.val)

            if level % 2 == 1:
                while queue and temp:
                    node = queue.pop(0)
                    node.val = temp.pop()
                    
            level += 1
            
        return root