class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Finds the largest unique number in an unsorted array of integers.
        
        :param nums: List[int] - Unsorted array of integers
        :return: int - Largest unique number or -1 if no unique number exists
        """
        # Count occurrences of each number using a dictionary
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Filter out numbers that are not unique and find the maximum
        unique_nums = [num for num, count in num_count.items() if count == 1]
        return max(unique_nums) if unique_nums else -1