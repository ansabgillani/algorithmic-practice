class Solution:
    def rotate_string(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)