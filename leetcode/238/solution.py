class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left_products = [1] * n
        right_product = 1
        
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        for i in range(n - 1, -1, -1):
            left_products[i] *= right_product
            right_product *= nums[i]
        
        return left_products

# Example usage:
print(Solution().productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
print(Solution().productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]