class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Check if string 's' can become 'goal' after some number of shifts.
        
        :param s: Original string
        :param goal: Target string after shifts
        :return: True if 's' can become 'goal', False otherwise
        """
        return len(s) == len(goal) and goal in (s + s)