class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        
        for i in range(len(s2) - len_s1 + 1):
            if self._count_chars(s2[i:i+len_s1]) == self._count_chars(s1):
                return True

        return False
    
    def _count_chars(self, s: str) -> dict:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count