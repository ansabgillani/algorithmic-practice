class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Initialize score and a list to keep track of marked elements
        score = 0
        marked = [False] * len(nums)
        
        # Iterate until all elements are marked
        while sum(marked) < len(nums):
            min_val = float('inf')
            min_index = -1
            
            # Find the smallest unmarked element
            for i in range(len(nums)):
                if not marked[i] and nums[i] < min_val:
                    min_val = nums[i]
                    min_index = i
            
            # Mark the chosen element and its adjacent elements
            score += min_val
            marked[min_index] = True
            if min_index > 0:
                marked[min_index - 1] = True
            if min_index < len(nums) - 1:
                marked[min_index + 1] = True
        
        return score

# Example usage:
sol = Solution()
print(sol.findScore([2, 1, 3, 4, 5, 2]))  # Output: 7
print(sol.findScore([2, 3, 5, 1, 3, 2]))  # Output: 5