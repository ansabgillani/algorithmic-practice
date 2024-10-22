class Solution:
    def __init__(self):
        pass

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        queue = [root]
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heapq.heappush(level_sums, -level_sum)
            if len(level_sums) > k:
                heapq.heappop(level_sums)
        return -heappop(level_sums) if len(level_sums) == k else -1