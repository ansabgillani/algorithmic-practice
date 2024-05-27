class Solution:
    def minArrayEnd(self, n, x):
        ans = x
        while n > 0:
            if ans & (ans + 1) == ans:
                ans += 1 << (len(bin(ans)) - 3)
            else:
                ans += 1
            n -= 1
        return ans

# Example usage:
sol = Solution()
print(sol.minArrayEnd(3, 4))  # Output: 6
print(sol.minArrayEnd(2, 7))  # Output: 15