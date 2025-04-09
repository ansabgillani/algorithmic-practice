class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If k is greater than any element in nums, it's impossible to make all elements equal to k
        if max(nums) < k:
            return -1
        
        operations = 0
        while True:
            valid_h_found = False
            for h in range(k + 1, max(nums) + 1):
                valid = True
                for num in nums:
                    if num > h and num != max([num2 for num2 in nums if num2 > h]):
                        valid = False
                        break
                if valid:
                    valid_h_found = True
                    for i in range(len(nums)):
                        if nums[i] > h:
                            nums[i] = h
                    operations += 1
                    break
            
            # Check if all elements are now equal to k
            if all(num == k for num in nums):
                return operations
            
            # If no valid h is found and not all elements are equal to k, it's impossible
            if not valid_h_found:
                return -1