def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k <= 1:
        return 0
    
    left = 0
    product = 1
    count = 0
    
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k:
            product /= nums[left]
            left += 1
        
        count += right - left + 1
    
    return count

# Example test cases
print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # Output: 8
print(numSubarrayProductLessThanK([1, 2, 3], 0))        # Output: 0