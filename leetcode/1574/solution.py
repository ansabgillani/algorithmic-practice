class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        i, j = 0, n - 1

        while i + 1 < n and arr[i] <= arr[i+1]:
            i += 1

        if i == n - 1:
            return 0

        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1

        ans = min(n - i - 1, j)
        
        l, r = 0, j
        while l <= i and r < n:
            if arr[l] <= arr[r]:
                ans = min(ans, r - l - 1)
                l += 1
            else:
                r += 1

        return ans