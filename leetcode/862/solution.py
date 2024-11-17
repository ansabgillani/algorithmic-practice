class Solution:
    def shortestSubarray(self, nums, k):
        queue = [[0, 0]]
        prefix_sum = 0
        result = float('inf')
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            while queue and prefix_sum - queue[0][0] >= k:
                _, start_index = queue.popleft()
                result = min(result, i - start_index + 1)
            
            while queue and prefix_sum <= queue[-1][0]:
                queue.pop()
        
            queue.append([prefix_sum, i])
    
        return result if result != float('inf') else -1