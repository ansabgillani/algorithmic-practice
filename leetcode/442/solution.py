class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Finds all elements that appear twice in the input array.
        
        :param nums: List of integers where each integer is in the range [1, n] and appears at most twice.
        :return: List of integers that appear twice.
        """
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] *= -1
        return result

# Example usage:
# sol = Solution()
# print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Output: [2, 3]