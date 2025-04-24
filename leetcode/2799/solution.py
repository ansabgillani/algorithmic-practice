from collections import Counter, defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total_unique = len(set(nums))
        count = defaultdict(int)
        prefix_count = {0: 1}
        result = 0
        
        for num in nums:
            count[num] += 1
            current_unique = sum(1 for freq in count.values() if freq == 1)
            if current_unique >= total_unique:
                while current_unique > total_unique:
                    first_num = next(iter(count))
                    count[first_num] -= 1
                    if not count[first_num]:
                        del count[first_num]
                    current_unique = sum(1 for freq in count.values() if freq == 1)
                result += prefix_count[len(count)]
            prefix_count[len(count)] = prefix_count.get(len(count), 0) + 1
        
        return result