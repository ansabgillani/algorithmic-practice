class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Count numbers with even number of digits
        return sum(1 for num in nums if len(str(num)) % 2 == 0)