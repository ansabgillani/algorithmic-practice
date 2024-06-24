class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        current_flips = 0
        flips = [0] * (n + 1)
        
        for i in range(n):
            current_flips += flips[i]
            if (nums[i] + current_flips) % 2 == 0:
                if i + k > n:
                    return -1
                flips[i] += 1
                current_flips += 1
                flip_count += 1
        
        return flip_count