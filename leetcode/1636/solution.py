from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        
        # Sort numbers first by increasing frequency, then by decreasing value
        return sorted(nums, key=lambda x: (count[x], -x))