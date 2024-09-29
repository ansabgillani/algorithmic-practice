class Solution:
    def minimumAbsDifference(self, arr):
        """
        Finds all pairs of elements with the minimum absolute difference in an array.
        
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if not arr or len(arr) < 2:
            return []
        
        # Sort the array to make sure the smallest differences are adjacent
        arr.sort()
        min_diff = float('inf')
        result = []
        
        # Iterate through the sorted array and find the minimum difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i-1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result