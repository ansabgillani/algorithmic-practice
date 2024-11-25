class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(i):
            return (i + nums[i]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            is_forward = nums[i] > 0
            slow, fast = i, next_index(i)
            
            while nums[fast] * nums[i] > 0 and nums[next_index(fast)] * nums[i] > 0:
                if slow == fast:
                    if slow != next_index(slow):
                        return True
                    break
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            
            slow, mark = i, -nums[i]
            while nums[slow] * mark < 0:
                temp = next_index(slow)
                nums[slow] = mark
                slow = temp
        
        return False

# Example usage:
solution = Solution()
print(solution.circularArrayLoop([2, -1, 1, 2, 2]))  # Output: True
print(solution.circularArrayLoop([-1, -2, -3, -4, -5, 6]))  # Output: False
print(solution.circularArrayLoop([1, -1, 5, 1, 4]))  # Output: True