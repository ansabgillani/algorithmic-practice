class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Returns the number of non-empty subarrays that have a sum divisible by k.
        
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        cumulative_sum = 0
        remainder_count = {0: 1}  # Initialize with remainder 0 having one occurrence
        
        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))  # Output: 7
# print(sol.subarraysDivByK([5], 9))  # Output: 0