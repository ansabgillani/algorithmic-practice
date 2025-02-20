class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Given an array of strings nums containing n unique binary strings each of length n,
        return a binary string of length n that does not appear in nums.
        
        :param nums: List of unique binary strings
        :return: A unique binary string not present in nums
        """
        # Create a set for quick lookup of existing numbers
        num_set = set(nums)
        
        # Iterate through all possible binary strings of length n
        for i in range(2**len(nums)):
            bin_str = format(i, f'0{len(nums)}b')
            if bin_str not in num_set:
                return bin_str

# Example usage:
# solution = Solution()
# print(solution.findDifferentBinaryString(["01", "10"]))  # Output: "11" or "00"