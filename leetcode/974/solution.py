class Solution:
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainder_count = {0: 1}
        total_sum = result = 0
        
        for num in nums:
            total_sum += num
            remainder = total_sum % k
            
            if remainder < 0:
                remainder += k
            
            result += remainder_count.get(remainder, 0)
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return result