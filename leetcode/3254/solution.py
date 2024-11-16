class Solution:
    def findPowerOfKSizeSubarrays(self, nums, k):
        n = len(nums)
        results = [-1] * (n - k + 1)

        for i in range(n - k + 1):
            subarray = nums[i:i+k]

            # Check if the subarray is sorted and consecutive
            if all(subarray[j] <= subarray[j+1] for j in range(k-1)) and len(set(subarray)) == k:
                results[i] = max(subarray)

        return results