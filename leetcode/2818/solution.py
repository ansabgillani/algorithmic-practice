class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Function to calculate prime score of a number
        def prime_score(x):
            count = 0
            if x % 2 == 0:
                count += 1
                while x % 2 == 0:
                    x //= 2
            for i in range(3, int(sqrt(x)) + 1, 2):
                if x % i == 0:
                    count += 1
                    while x % i == 0:
                        x //= i
            if x > 2:
                count += 1
            return count
        
        # Calculate prime scores for all numbers in nums
        scores = [prime_score(num) for num in nums]
        
        # Stack to find the next greater element on the left and right
        left, right = [-1] * len(nums), [len(nums)] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and scores[stack[-1]] < scores[i]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        # Calculate the maximum score
        max_score = 0
        for i in range(len(nums)):
            length = (i - left[i]) * (right[i] - i)
            operations = min(length, k)
            k -= operations
            max_score = (max_score * pow(nums[i], operations, MOD)) % MOD
            if k == 0:
                break
        
        return max_score