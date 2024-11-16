class Solution:
    def findPowerOfKSizeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1] * (n - k + 1)

        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            if self.isConsecutiveAndSorted(subarray):
                results[i] = max(subarray)

        return results

    def isConsecutiveAndSorted(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] != sorted_arr[i-1] + 1:
                return False
        return True