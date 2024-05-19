class Solution:
    def maxSum(self, nums, k, edges):
        greater = sum(1 for num in nums if num < num ^ k)
        smaller = len(nums) - greater
        
        max_sum = sum(max(num, num ^ k) for num in nums)
        
        if greater > smaller:
            return max_sum + 2 * (k - min(nums))
        
        return max_sum