class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        Finds the length of the shortest subarray that can be removed to make the array non-decreasing.
        
        :param arr: List[int] - The input array of integers.
        :return: int - The length of the shortest subarray to remove.
        """
        n = len(arr)
        left, right = 0, n - 1
        
        # Find the first out-of-order element from the left
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the array is already non-decreasing
        if left == n - 1:
            return 0
        
        # Find the first out-of-order element from the right
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Try removing subarray from the left to make the remaining array sorted
        result = min(n - (left + 1), right)
        
        # Merge the two parts by moving pointers and updating result
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result

# Example usage:
sol = Solution()
print(sol.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))  # Output: 3
print(sol.findLengthOfShortestSubarray([5,4,3,2,1]))        # Output: 4
print(sol.findLengthOfShortestSubarray([1,2,3]))            # Output: 0