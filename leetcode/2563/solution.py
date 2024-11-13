class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort the array to facilitate binary search
        nums.sort()
        
        def atMost(limit):
            i, ans = 0, 0
            for j in range(len(nums)):
                while i <= j and nums[i] + nums[j] > limit:
                    i += 1
                ans += max(j - i, 0)
            return ans
        
        # Count pairs with sum less than or equal to upper
        count_upper = atMost(upper)
        
        # Count pairs with sum less than lower
        count_lower = atMost(lower - 1)
        
        # The difference gives the count of fair pairs
        return count_upper - count_lower