class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        sieve = [True] * 1001
        for x in range(2, int(1000 ** 0.5) + 1):
            if sieve[x]:
                for i in range(x*x, 1001, x):
                    sieve[i] = False

        primes = [x for x in range(2, 1001) if sieve[x]]

        def find_smallest_prime(n: int) -> int:
            return next((p for p in primes if p < n), 0)

        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i-1]:
                diff = nums[i] - nums[i-1] + 1
                p = find_smallest_prime(diff)
                nums[i] -= p

        return all(nums[i] < nums[i+1] for i in range(len(nums)-1))