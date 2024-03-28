class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Returns the length of the longest good subarray where each element's frequency is at most k.
        
        :param nums: List[int] - The input array of integers.
        :param k: int - The maximum allowed frequency for each element in a subarray.
        :return: int - The length of the longest good subarray.
        """
        # Dictionary to store the frequency of elements in the current window
        freq = {}
        left = 0
        max_length = 0
        
        for right, num in enumerate(nums):
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            # If any element's frequency exceeds k, shrink the window from the left
            while freq[num] > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            # Update the maximum length of the good subarray
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example test cases
solution = Solution()
print(solution.maxSubarrayLength([1,2,3,1,2,3,1,2], k=2))  # Output: 6
print(solution.maxSubarrayLength([1,2,1,2,1,2,1,2], k=1))  # Output: 2
print(solution.maxSubarrayLength([5,5,5,5,5,5,5], k=4))    # Output: 4