class Solution:
    def findScore(self, nums):
        n = len(nums)
        marked = [False] * n
        score = 0
        
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        
        while heap:
            value, index = heapq.heappop(heap)
            
            if marked[index]:
                continue
            
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < n - 1:
                marked[index + 1] = True
        
            score += value
        
        return score

# Example usage
solution = Solution()
print(solution.findScore([2,1,3,4,5,2]))  # Output: 7
print(solution.findScore([2,3,5,1,3,2]))  # Output: 5