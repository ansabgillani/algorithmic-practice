class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        total_balls, left_sum = boxes.count('1'), 0
        
        ans = [0] * n
        
        right_sum = total_balls - int(boxes[0])
        for i in range(n):
            ans[i] += abs(i) * right_sum - left_sum
            left_sum += int(boxes[i])
        
        return ans