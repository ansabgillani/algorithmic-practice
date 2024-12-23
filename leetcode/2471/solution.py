class Solution:
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        operations = 0
        
        while queue:
            size = len(queue)
            level_values = []
            
            # Collect all node values at the current level
            for _ in range(size):
                node = queue.popleft()
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            # Sort the collected values and count operations to sort them
            sorted_values = sorted(level_values)
            visited = [False] * size
            
            for i in range(size):
                while level_values[i] != sorted_values[i]:
                    j = next(j for j in range(i, size) if not visited[j] and level_values[j] == sorted_values[i])
                    level_values[i], level_values[j] = level_values[j], level_values[i]
                    operations += 1
                    visited[j] = True
                    
        return operations