class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        Given a sorted integer array nums and an integer n,
        add/patch elements to the array such that any number in the range [1, n] inclusive 
        can be formed by the sum of some elements in the array. Return the minimum number 
        of patches required.
        
        :param nums: List[int]
        :param n: int
        :return: int
        """
        patches = 0
        i = 0
        miss = 1
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        
        return patches

# Example usage:
sol = Solution()
print(sol.minPatches([1,3], 6))  # Output: 1
print(sol.minPatches([1,5,10], 20))  # Output: 2
print(sol.minPatches([1,2,2], 5))  # Output: 0