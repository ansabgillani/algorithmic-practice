class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        queue = deque([root])
        level_sums = []
        
        while queue:
            level_size = len(queue)
            current_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(current_sum)
        
        if len(level_sums) < k:
            return -1
        
        level_sums.sort(reverse=True)
        return level_sums[k-1]