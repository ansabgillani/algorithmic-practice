class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element using Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Step 2: Verify that the candidate is indeed the dominant element
        total_count = nums.count(candidate)
        
        # If the candidate is not the dominant element, return -1 (though problem guarantees one dominant element)
        if total_count <= len(nums) // 2:
            return -1
        
        # Step 3: Find the minimum valid split index
        left_count = 0
        
        for i in range(len(nums)):
            if nums[i] == candidate:
                left_count += 1
            
            right_count = total_count - left_count
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - i - 1):
                return i
        
        return -1