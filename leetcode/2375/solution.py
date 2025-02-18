class Solution:
    def smallestNumber(self, pattern):
        result = []
        stack = []
        
        current_value = 1
        stack.append(current_value)
        
        for char in pattern:
            if char == 'I':
                while len(stack) > 0:
                    result.append(str(stack.pop()))
                current_value += 1
                stack.append(current_value)
            else:
                stack.append(current_value + 1)
                current_value += 1
        
        result.append(str(stack[0]))
        
        while len(stack) > 1:
            result.append(str(stack.pop()))
        
        return ''.join(result)