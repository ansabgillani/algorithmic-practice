class Solution:
    def punishment_number(self, n):
        def is_partitioned(num, target, i=0, curr_sum=0, start=0):
            if curr_sum == target and i == len(str(num)):
                return True
            if curr_sum > target or i > len(str(num)):
                return False
            
            for j in range(start, len(str(num))):
                sub_num = int(str(num)[i:j+1])
                if is_partitioned(num, target, i=j+1, curr_sum=curr_sum + sub_num):
                    return True
        
            return False
        
        total_punishment = 0
        for i in range(1, n + 1):
            if is_partitioned(i**2, i):
                total_punishment += i**2
            
        return total_punishment

# Testing the method with provided examples
solution = Solution()
print(solution.punishment_number(10))  # Output: 182
print(solution.punishment_number(37))  # Output: 1478