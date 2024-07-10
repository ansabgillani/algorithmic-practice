class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        Calculates the minimum number of operations needed to go back to the main folder after performing change folder operations.
        
        :param logs: List of strings representing file system operations
        :return: Minimum number of operations needed to return to the main folder
        """
        depth = 0
        
        for log in logs:
            if log == '../':
                depth = max(0, depth - 1)
            elif log != './':
                depth += 1
                
        return depth