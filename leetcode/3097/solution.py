class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix_or = [0] * (n + 1)  
        for i in range(n):
            prefix_or[i + 1] = prefix_or[i] | nums[i]
        
        ans = float('inf')
        queue = deque()  
        
        for i, cur_or in enumerate(prefix_or):
            while queue and cur_or - prefix_or[queue[0]] >= k:
                start = queue.popleft()
                ans = min(ans, i - start)
            
            while queue and cur_or <= prefix_or[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        return ans if ans != float('inf') else -1