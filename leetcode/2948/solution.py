class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_indices = sorted(range(n), key=lambda x: nums[x])
        ans = [-1] * n
        
        buckets = defaultdict(list)
        for i, idx in enumerate(sorted_indices):
            if i > 0 and nums[idx] - nums[sorted_indices[i-1]] <= limit:
                buckets[nums[idx]].append(idx)
            else:
                for bucket_idx in buckets[nums[idx]]:
                    ans[bucket_idx] = nums[bucket_idx]
                buckets[nums[idx]] = [idx]

        for bucket_idx in buckets[nums[-1]]:
            ans[bucket_idx] = nums[bucket_idx]
        
        return ans