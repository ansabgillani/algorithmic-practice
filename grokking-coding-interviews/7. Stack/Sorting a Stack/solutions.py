class Solution:
    def sortStack(self, stack: List[int]) -> None:
        """
        Sorts a stack in ascending order using another temporary stack.
        
        :param stack: List of integers to be sorted
        """
        temp_stack = []
        
        while stack:
            # Pop the top element from main stack
            temp = stack.pop()
            
            # Push elements from temp_stack back into main stack if they are greater than temp
            while temp_stack and temp_stack[-1] > temp:
                stack.append(temp_stack.pop())
            
            # Push the temp element into temp_stack
            temp_stack.append(temp)
        
        # Transfer all elements from temp_stack to stack to get them in sorted order
        while temp_stack:
            stack.append(temp_stack.pop())