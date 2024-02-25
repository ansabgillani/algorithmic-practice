import math
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        # Special case: if any number is 1, it cannot form a traversal
        if 1 in nums:
            return False
        
        # Sieve of Eratosthenes to find prime factors up to the maximum number
        max_num = max(nums)
        primes = [True] * (max_num + 1)
        for i in range(2, int(math.sqrt(max_num)) + 1):
            if primes[i]:
                for j in range(i*i, max_num + 1, i):
                    primes[j] = False
        
        # Dictionary to store the smallest prime factor for each number
        spf = {}
        for num in nums:
            for i in range(2, num + 1):
                if primes[i] and num % i == 0:
                    spf[num] = i
                    break
        
        # Union-Find data structure to group numbers by their prime factors
        parent = {num: num for num in nums}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        
        # Group numbers by their smallest prime factor
        factor_to_numbers = defaultdict(list)
        for num in nums:
            factor_to_numbers[spf[num]].append(num)
        
        # Union all numbers that share the same smallest prime factor
        for group in factor_to_numbers.values():
            first_num = group[0]
            for num in group[1:]:
                union(first_num, num)
        
        # Check if all numbers belong to the same group
        root_set = set(find(num) for num in nums)
        return len(root_set) == 1

# Example usage:
# sol = Solution()
# print(sol.canTraverseAllPairs([2,3,6]))  # Output: True
# print(sol.canTraverseAllPairs([3,9,5]))  # Output: False
# print(sol.canTraverseAllPairs([4,3,12,8]))  # Output: True