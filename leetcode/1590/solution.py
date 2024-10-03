def minSubarray(nums, p):
    total_sum = sum(nums)
    target = total_sum % p
    if target == 0:
        return 0
    
    prefix_sum_mod = {0: -1}
    current_sum_mod = 0
    min_length = len(nums) + 1
    
    for i, num in enumerate(nums):
        current_sum_mod = (current_sum_mod + num) % p
        required_mod = (current_sum_mod - target) % p
        
        if required_mod in prefix_sum_mod:
            subarray_length = i - prefix_sum_mod[required_mod]
            min_length = min(min_length, subarray_length)
        
        prefix_sum_mod[current_sum_mod] = i
    
    return min_length if min_length < len(nums) else -1