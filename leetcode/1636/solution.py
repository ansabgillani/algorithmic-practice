class Solution:
    def frequencySort(self, nums):
        count = {}
        
        # Count the frequency of each number in nums
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # Sort the array based on increasing frequency and decreasing value if frequencies are equal
        return sorted(nums, key=lambda x: (count[x], -x))