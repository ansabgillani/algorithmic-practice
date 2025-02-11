class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Finds all duplicates in an array of integers where each integer is between 1 and n (inclusive).
        
        This function runs in O(n) time complexity with constant space complexity.
        
        :param nums: List[int] - List of integers
        :return: List[int] - List of duplicate integers
        """
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(index + 1))
            else:
                nums[index] *= -1
        
        return result