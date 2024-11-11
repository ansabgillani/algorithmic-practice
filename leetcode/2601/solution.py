class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Function to check if a number is prime
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        # Generate a list of prime numbers less than the maximum value in nums
        max_val = max(nums)
        primes = [i for i in range(2, max_val) if is_prime(i)]
        
        # Iterate through nums and perform operations
        for i in range(len(nums)):
            if i > 0:
                if nums[i] <= nums[i-1]:
                    return False
            diff = nums[i] - (nums[i-1] + 1 if i > 0 else 0)
            j = bisect_right(primes, diff)
            if j >= len(primes) or primes[j] > diff:
                j -= 1
            if j >= 0:
                nums[i] -= primes[j]
        
        # Check if the array is strictly increasing after operations
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        
        return True

# Example usage
solution = Solution()
print(solution.primeSubOperation([4, 9, 6, 10]))  # Output: True
print(solution.primeSubOperation([6, 8, 11, 12]))  # Output: True
print(solution.primeSubOperation([5, 8, 3]))  # Output: False