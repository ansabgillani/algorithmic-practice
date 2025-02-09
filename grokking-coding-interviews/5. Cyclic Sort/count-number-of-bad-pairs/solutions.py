class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Count the number of bad pairs in the given array.
        
        A pair (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
        
        :param nums: List of integers
        :return: Total number of bad pairs
        """
        n = len(nums)
        good_pairs_count = 0
        
        # Calculate the number of good pairs first
        for i in range(n):
            for j in range(i + 1, n):
                if j - i == nums[j] - nums[i]:
                    good_pairs_count += 1
                    
        # Total pairs minus good pairs gives bad pairs
        return (n * (n - 1) // 2) - good_pairs_count

# Test cases to verify the solution
def test_solution():
    sol = Solution()
    
    assert sol.countBadPairs([4,1,3,3]) == 5, "Test case 1 failed"
    assert sol.countBadPairs([1,2,3,4,5]) == 0, "Test case 2 failed"
    assert sol.countBadPairs([1,3,2,4,5,6]) == 9, "Test case 3 failed"

test_solution()