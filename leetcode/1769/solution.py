class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left_operations = [0] * n
        right_operations = [0] * n
        
        balls_left = 0
        balls_right = sum(int(b) for b in boxes)
        
        for i in range(n):
            if boxes[i] == '1':
                balls_left += 1
            
            left_operations[i] = balls_left * i
        
            if boxes[n - 1 - i] == '1':
                balls_right -= 1
            
            right_operations[n - 1 - i] = balls_right * (n - i - 1)
        
        return [left + right for left, right in zip(left_operations, right_operations)]