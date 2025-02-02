class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Check if the array was originally sorted in non-decreasing order and rotated.
        
        :param nums: List of integers
        :return: True if sorted and rotated, False otherwise
        """
        n = len(nums)
        count = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        
        return True