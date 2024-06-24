class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_needed = 0
        flip_count = [0] * (n + 1)

        for i in range(n):
            flip_needed += flip_count[i]
            if (nums[i] + flip_needed) % 2 == 0:
                if i + k > n:
                    return -1
                nums[i] = 1
                flip_count[i + 1] += 1

        if all(nums):
            return sum(flip_needed > i for i in range(n))
        else:
            return -1