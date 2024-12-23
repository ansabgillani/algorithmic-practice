class Solution:
    def minimumOperations(self, root: TreeNode) -> int:
        from collections import deque
        
        def min_swaps_to_sorted(arr):
            visited = {v: i for i, v in enumerate(sorted(arr))}
            swaps = 0
            arr_pos = {i: v for i, v in enumerate(arr)}
            
            for i in range(len(arr)):
                if arr[i] != sorted(arr)[i]:
                    to_swap_idx = visited[arr[i]]
                    
                    # Swap elements
                    arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
                    visited[arr[to_swap_idx]] = to_swap_idx
                    
                    swaps += 1
            
            return swaps
        
        def dfs(node):
            if not node:
                return 0
            
            queue = deque([node])
            operations = 0
            
            while queue:
                level_size = len(queue)
                level_values = []
                
                for _ in range(level_size):
                    current_node = queue.popleft()
                    level_values.append(current_node.val)
                    
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                
                operations += min_swaps_to_sorted(level_values)
            
            return operations
        
        return dfs(root)