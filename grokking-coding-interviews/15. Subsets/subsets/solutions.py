class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given list of unique integers.
        
        :param nums: List of unique integers
        :return: List of lists containing all possible subsets
        """
        result = []
        self backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, start, current, result):
        """
        Helper function to perform backtracking.
        
        :param nums: Input list of unique integers
        :param start: Starting index for the current subset
        :param current: Current subset being built
        :param result: List to store all subsets
        """
        result.append(current)
        for i in range(start, len(nums)):
            self.backtrack(nums, i + 1, current + [nums[i]], result)