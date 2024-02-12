class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the array which appears more than n/2 times.
        
        This implementation uses the Boyer-Moore Voting Algorithm to find the majority element
        in linear time O(n) and constant space O(1).
        
        :param nums: List of integers where the majority element exists.
        :return: The majority element.
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate